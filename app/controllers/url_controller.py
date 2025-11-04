from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.schemas.url_schema import URLCreate, URLResponse
from app.core.database import get_db
from app.repositories.url_repository import URLRepository
from app.services.url_service import URLService

router = APIRouter(prefix="/urls", tags=["URLs"])


@router.post("/", response_model=URLResponse)
def create_short_url(data: URLCreate, db: Session = Depends(get_db)):
    repo = URLRepository(db)
    service = URLService(repo)
    return service.create_short_url(data.url)


@router.get("/{code}")
def redirect_url(code: str, db: Session = Depends(get_db)):
    repo = URLRepository(db)
    service = URLService(repo)
    url = service.get_and_increment(code)
    return RedirectResponse(url.original_url)


@router.get("/stats/{code}", response_model=URLResponse)
def stats(code: str, db: Session = Depends(get_db)):
    repo = URLRepository(db)
    service = URLService(repo)
    return service.get_stats(code)
