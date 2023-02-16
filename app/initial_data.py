import asyncio
import logging

from app.database.seed import init_db
from app.database.database import SessionLocal


def init():
    db = SessionLocal()
    init_db(db)


def main():
    logging.info("Creating seed")
    init()
    logging.info("Seed user created")


if __name__ == "__main__":
    asyncio.run(main())
