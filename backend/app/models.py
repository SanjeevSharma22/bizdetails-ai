from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, JSON
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    organization = relationship("Organization", back_populates="users")


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    credit_allocated = Column(Integer, default=0)
    users = relationship("User", back_populates="organization")
    credit_usage = relationship("CreditUsage", back_populates="organization")


class CreditUsage(Base):
    __tablename__ = "credit_usage"

    id = Column(Integer, primary_key=True)
    org_id = Column(Integer, ForeignKey("organizations.id"))
    used = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
    organization = relationship("Organization", back_populates="credit_usage")


class EnrichmentJob(Base):
    __tablename__ = "enrichment_jobs"

    id = Column(Integer, primary_key=True)
    org_id = Column(Integer, ForeignKey("organizations.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")
    submitted_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    records = relationship("CompanyRecord", back_populates="job")


class CompanyRecord(Base):
    __tablename__ = "company_records"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("enrichment_jobs.id"))
    name = Column(String)
    domain = Column(String)
    industry = Column(String, nullable=True)
    keywords = Column(String, nullable=True)
    employee_size = Column(String, nullable=True)
    revenue = Column(String, nullable=True)
    enriched_data = Column(JSON, default={})
    job = relationship("EnrichmentJob", back_populates="records")
