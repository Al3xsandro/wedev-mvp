from fastapi import APIRouter, Query, Body, Depends, HTTPException, Request

from app.database.database import get_db
from sqlalchemy.orm import Session

from fastapi.templating import Jinja2Templates

from app.database.models import User
from app.api.middlewares import getCurrentUser

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get("/", include_in_schema=False)
def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(getCurrentUser),
):
    return templates.TemplateResponse("base.html", {"request": request})
