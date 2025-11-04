import string, random
from fastapi import HTTPException
from app.repositories.url_repository import URLRepository


class URLService:
    def __init__(self, repository: URLRepository):
        self.repository = repository

    def _generate_code(self, length: int = 6) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


    def create_short_url(self, original_url: str):
        code = self._generate_code()
        return self.repository.create(str(original_url), code)

    def get_and_increment(self, code: str):
        url = self.repository.get_by_code(code)
        if not url:
            raise HTTPException(status_code=404, detail="URL not found")
        self.repository.increment_clicks(url)
        return url

    def get_stats(self, code: str):
        url = self.repository.get_by_code(code)
        if not url:
            raise HTTPException(status_code=404, detail="URL not found")
        return url
