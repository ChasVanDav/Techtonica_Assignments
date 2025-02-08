# models.py

from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_title = Column(String, unique=True, nullable=False)
    video_id = Column(String, nullable=True)
    video_url = Column(String, nullable=True)
    video_title = Column(String, nullable=True)
    video_metadata = Column(JSON, nullable=True)  # Stores video details like views, duration
