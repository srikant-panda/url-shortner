from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from models.url import Urls
from db import get_db
from schemas.url_schema import Urlcreate, Urlresponse
from services.url_service import create_short_url

router = APIRouter()


@router.post("/shorten", response_model=Urlresponse)
def shorten_url(data: Urlcreate, db: Session = Depends(get_db)):

    url = create_short_url(db, data.url)

    return url

@router.get("/{code}")
def redirect_url(code : str ,db: Session = Depends(get_db)):
    
    query = db.query(Urls).filter(Urls.short_code == code).first()
    if query is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(query.url)

