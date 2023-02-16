import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = "39e9ee9b41bcb2e444d4086f12a50d2f"  # must be in env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

DEFAULT_USER = "staff@admin.com"
DEFAULT_PASSWORD = "hardpassword"
