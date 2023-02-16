from fastapi import APIRouter

from app.api.endpoints import session, courses, users
from app.api.views import session_views, users_views


routes = APIRouter()

# api
routes.include_router(session.router, prefix="/session", tags=["Autenticação"])
routes.include_router(users.router, prefix="/users", tags=["Usuários"])
routes.include_router(courses.router, prefix="/courses", tags=["Cursos"])

# views
routes.include_router(session_views.router)
routes.include_router(session_views.router)
