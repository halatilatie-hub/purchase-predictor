from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.get("/receipts")
def get_receipts():
    return {"items": [], "message": "Receipt history endpoint ready"}


@router.post("/receipts/upload")
async def upload_receipt(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Receipt received and queued for processing",
    }
