# https://stackoverflow.com/questions/63420889/fastapi-pydantic-circular-references-in-separate-files
from .user import User
from .phoneNumber import PhoneNumber
from .course import Course
from .courseLike import CourseLike
from .studentCourse import StudentCourse
