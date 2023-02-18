#!/usr/bin/bash
export PYTHONPATH=$PYTHONPATH:/app

# run migrations
alembic upgrade head

# run initial data
python3 app/initial_data.py