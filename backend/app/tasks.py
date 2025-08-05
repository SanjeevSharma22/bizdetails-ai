from celery import Celery
from .config import settings

celery = Celery(__name__, broker=settings.redis_url)


def process_enrichment(contents: bytes):
    # Placeholder for CSV parsing and enrichment logic
    pass


@celery.task
def enrich_companies(job_id: str, file_path: str):
    # TODO: Implement enrichment logic
    return
