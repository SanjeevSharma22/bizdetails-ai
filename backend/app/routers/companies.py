from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..db import get_db

router = APIRouter()


@router.get("/search")
def search_companies(name: str | None = None, domain: str | None = None, db: Session = Depends(get_db)):
    if not name and not domain:
        return []
    query = db.query(models.CompanyRecord)
    if name:
        query = query.filter(models.CompanyRecord.name.ilike(f"%{name}%"))
    if domain:
        query = query.filter(models.CompanyRecord.domain.ilike(f"%{domain}%"))
    return query.limit(50).all()
