from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from ..tasks import process_enrichment

router = APIRouter()


@router.post("/upload")
async def upload_csv(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    contents = await file.read()
    background_tasks.add_task(process_enrichment, contents)
    return {"status": "submitted"}


@router.get("/jobs/{job_id}")
def job_status(job_id: int):
    return {"job_id": job_id, "status": "pending"}


@router.get("/jobs/{job_id}/results")
def job_results(job_id: int):
    return []
