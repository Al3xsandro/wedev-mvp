from fastapi import APIRouter, Body, Depends, HTTPException

from app.database.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/:id", name="Acessar curso", description="Acessar curso cadastrado")
def get_course(id: int, db: Session = Depends(get_db)):
    return {"id": 1}
