from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from .database import Base
import enum
from sqlalchemy import Enum


class PostStatus(str, enum.Enum):
    draft = "draft"
    scheduled = "scheduled"
    published = "published"
    approved = "approved"

class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tone = Column(String)
    target_audience = Column(String)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    caption = Column(Text)
    image_path = Column(String)
    status = Column(Enum(PostStatus), default="draft")
    scheduled_at = Column(DateTime, nullable = True)


class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer)
    impressions = Column(Integer)
    clicks = Column(Integer)
    engagement_rate = Column(Float)
