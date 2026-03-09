from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db import Base

class Urls(Base):
    __tablename__ = "url"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    url: Mapped[str] = mapped_column(String, nullable=False)
    short_code: Mapped[str] = mapped_column(String, unique=True, index=True)