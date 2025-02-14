# only need to run this once to create database tables

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from database import engine, Base  # Import engine and Base from your database.py

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define your Recipe model here
from models import Recipe  # Import your Recipe model here

# This will create all the tables in the database, including 'recipes'
Base.metadata.create_all(engine)

print("Database and tables created successfully.")
