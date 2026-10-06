from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads" / "receipts"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024

app = FastAPI(title="Purchase Predictor API")

# Allow your React frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Purchase Predictor API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload-receipt")
async def upload_receipt(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected.")

    suffix = Path(file.filename).suffix.lower()
    content_type = (file.content_type or "").lower()

    if suffix not in ALLOWED_EXTENSIONS or content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed (jpg, jpeg, png, webp).",
        )

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=400,
            detail="File exceeds the 10 MB limit.",
        )

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    saved_name = file.filename
    saved_path = UPLOAD_DIR / saved_name
    saved_path.write_bytes(contents)

    return {
        "status": "uploaded",
        "filename": file.filename,
        "saved_filename": saved_name,
        "content_type": content_type,
        "size": len(contents),
        "message": "Receipt uploaded successfully",
    }