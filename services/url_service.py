from sqlalchemy.orm import Session
from models.url import Urls
from utils import generate_code


def create_short_url(db: Session, long_url: str):

    code = generate_code()

    url = Urls(
        url=long_url,
        short_code=code
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url