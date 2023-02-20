from fastapi import APIRouter

from app.api.endpoints import session, courses, users


routes = APIRouter()

# api
routes.include_router(session.router, prefix="/session", tags=["Autenticação"])
routes.include_router(users.router, prefix="/users")
routes.include_router(courses.router, prefix="/courses")
