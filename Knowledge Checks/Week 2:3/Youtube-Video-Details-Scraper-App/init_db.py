from database import engine, Base

# This creates all tables in the database
Base.metadata.create_all(engine)

print("Database and tables created successfully.")