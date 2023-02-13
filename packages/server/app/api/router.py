from fastapi import APIRouter
from app.api.endpoints import courses, users, session


routes = APIRouter()

routes.include_router(session.router, tags=["Autenticação"])
routes.include_router(users.router, prefix="/users", tags=["Usuários"])
routes.include_router(courses.router, prefix="/courses", tags=["Cursos"])


@routes.get("/", include_in_schema=False)
def start():
    return {"version": "1.0"}
