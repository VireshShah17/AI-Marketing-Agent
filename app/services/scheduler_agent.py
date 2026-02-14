from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models
from .publisher_agent import publish_post
from .analytics_agent import generate_analytics
from ..logger import logger

scheduler = BackgroundScheduler()


def check_scheduled_posts():
    db: Session = SessionLocal()
    posts = db.query(models.Post).filter(models.Post.status == "scheduled").all()
    for post in posts:
        if post.scheduled_at <= datetime.utcnow():
            publish_post(post)
            post.status = "published"
            logger.info(f"Published post ID {post.id} for brand ID {post.brand_id}")
            generate_analytics(db, post)
            db.commit()
    
    db.close


def start_scheduler():
    scheduler.add_job(check_scheduled_posts, "interval", seconds = 60) # Check every minute
    scheduler.start()