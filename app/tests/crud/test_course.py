from sqlalchemy.orm import Session

import app.crud.course as crud
from app.schemas.course import CourseCreate

import pytest


def test_create_course_without_teacherId():
    with pytest.raises(Exception):
        CourseCreate(name="Course 1", is_active=True)
