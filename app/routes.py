from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import models
from .services.caption_agent import generate_caption
from .services.safety_agent import validate_caption
from .services.image_agent import generate_image
from .services.feedback_agent import generate_feedback_strategy
from datetime import datetime, timedelta


router = APIRouter()


@router.post("/brands/")
def create_brand(name: str, tone: str, target_audience: str, db: Session = Depends(get_db)):
    brand = models.Brand(name = name, tone = tone, target_audience = target_audience)
    db.add(brand)
    db.commit()
    db.refresh(brand)

    return brand


@router.post("/posts/generate")
def generate_post(brand_id: int, db: Session = Depends(get_db)):
    brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    if not brand:
        return {"error": "Brand not found"}
    
    caption = generate_caption(brand)
    is_safe, message = validate_caption(caption)
    image_path = generate_image(caption)

    if not is_safe:
        return {
            "error": "Safety validation failed",
            "reason": message
        }

    posts = models.Post(caption = caption, status = "draft", image_path = image_path)

    db.add(posts)
    db.commit()
    db.refresh(posts)

    return posts


@router.put("/posts/{post_id}/approve")
def approve_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        return {"error": "Post not found"}
    
    post.status = "approved"
    db.commit()

    return {"message": "Post approved"}


@router.get("/posts/")
def list_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@router.post("/posts/{post_id}/schedule")
def schedule_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id, models.Post.status == 'approved').first()
    if not post:
        return {"error": "Post not found or not approved"}
    
    post.status = "scheduled"
    post.scheduled_at = datetime.utcnow() + timedelta(minutes = 1) # Schedule for 1 minute later for testing
    db.commit()

    return {"message": "Post scheduled"}


@router.post("/posts/adaptive-generate/")
def adaptive_generate_post(brand_id: int, db: Session = Depends(get_db)):
    brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    if not brand:
        return {"error": "Brand not found"}

    # Get latest analytics
    latest_analytics = db.query(models.Analytics).order_by(models.Analytics.id.desc()).first()
    if not latest_analytics:
        return {"error": "No analytics available yet"}

    strategy = generate_feedback_strategy(latest_analytics)
    caption = generate_caption(brand, strategy)
    is_safe, message = validate_caption(caption)
    if not is_safe:
        return {"error": "Safety validation failed", "reason": message}

    image_path = generate_image(caption)
    post = models.Post(
        caption=caption,
        image_path=image_path,
        status="draft"
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return {
        "post": post,
        "applied_strategy": strategy
    }


@router.get("/brands/")
def list_brands(db: Session = Depends(get_db)):
    return db.query(models.Brand).all()


@router.delete("/brands/{brand_id}")
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    if not brand:
        return {"error": "Brand not found"}

    db.delete(brand)
    db.commit()

    return {"message": "Brand deleted"}

