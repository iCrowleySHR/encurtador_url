from sqlalchemy.orm import Session
from app.models.url_model import URLModel


class URLRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, original_url: str, short_code: str) -> URLModel:
        new_url = URLModel(original_url=original_url, short_code=short_code)
        self.db.add(new_url)
        self.db.commit()
        self.db.refresh(new_url)
        return new_url

    def get_by_code(self, short_code: str) -> URLModel | None:
        return self.db.query(URLModel).filter(URLModel.short_code == short_code).first()

    def increment_clicks(self, url: URLModel):
        url.clicks += 1
        self.db.commit()

    def get_all(self):
        return self.db.query(URLModel).all()
