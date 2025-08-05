from pydantic import BaseModel
from typing import Optional, Dict


class CompanyBase(BaseModel):
    name: Optional[str]
    domain: Optional[str]
    industry: Optional[str] = None
    keywords: Optional[str] = None
    employee_size: Optional[str] = None
    revenue: Optional[str] = None


class CompanyRecordOut(CompanyBase):
    id: int
    enriched_data: Dict | None = None

    class Config:
        orm_mode = True
