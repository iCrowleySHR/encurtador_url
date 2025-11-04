from fastapi import FastAPI
from app.core.database import Base, engine
from app.models.url_model import URLModel
from app.controllers.url_controller import router as url_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener API - POO")

app.include_router(url_router)
