from sqlmodel import create_engine, Session
from app.core.config import settings


# Database engine configuration for SQLModel
connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg2"
)

engine = create_engine(
    connection_string,
    echo=settings.DEBUG,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)


def get_session():
    """
    Dependency function to get database session for FastAPI endpoints.

    Yields:
        Session: Database session for use in endpoints
    """
    with Session(engine) as session:
        yield session