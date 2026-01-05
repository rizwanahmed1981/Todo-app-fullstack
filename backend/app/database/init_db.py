"""
Database initialization and table creation utilities.
"""
from sqlmodel import SQLModel
from app.database.database import engine
from app.models import User, Task
from app.core.config import settings


def create_tables():
    """
    Create all database tables for the application.
    """
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully.")


def drop_tables():
    """
    Drop all database tables (useful for testing).
    """
    print("Dropping database tables...")
    SQLModel.metadata.drop_all(engine)
    print("Database tables dropped successfully.")


def init_database():
    """
    Initialize the database with required tables and configurations.
    """
    print("Initializing database...")
    create_tables()
    print("Database initialized successfully.")


if __name__ == "__main__":
    # This can be used to initialize the database manually
    init_database()