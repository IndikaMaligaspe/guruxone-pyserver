"""
api.py
___

The REST API for guruxone-api
"""

from pathlib import Path

from fastapi import FastAPI

from .routes import members

app = FastAPI()


app.include_router(members.router, prefix="/member")

PROJECT_ROO = Path(__file__).parent.parent
