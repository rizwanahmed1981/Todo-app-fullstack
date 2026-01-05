import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import tasks, auth
from app.core.config import settings
from app.database.init_db import init_database


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="Todo Evolution API - Phase 2 Full-Stack Application",
    )

    @app.on_event("startup")
    def on_startup():
        init_database()

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.parsed_allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
    app.include_router(tasks.router, prefix="/api/{user_id}", tags=["tasks"])

    @app.get("/health")
    def health_check():
        """Health check endpoint to verify API is running."""
        return {"status": "healthy"}

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )