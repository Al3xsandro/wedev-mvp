from fastapi import APIRouter
from app.api.endpoints import courses, users, session


routes = APIRouter()

routes.include_router(session.router, tags=["Autenticação"])
routes.include_router(users.router, tags=["Usuários"])
routes.include_router(courses.router, tags=["Cursos"])


@routes.get("/version", include_in_schema=False)
def start():
    return {"version": "1.0"}
