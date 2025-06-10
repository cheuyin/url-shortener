import os
from datetime import datetime
from typing import Optional
from sqlalchemy import create_engine, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "database.db")
engine = create_engine(f"sqlite:///{db_path}", echo=True)


class Base(DeclarativeBase):
    pass


class ShortURL(Base):
    __tablename__ = "short_urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    alias: Mapped[str] = mapped_column(unique=True)
    original_url: Mapped[str]
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), insert_default=func.now()
    )


Base.metadata.create_all(engine)
