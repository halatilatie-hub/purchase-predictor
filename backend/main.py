from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

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
    # Placeholder — we'll wire OCR here next
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Receipt received (processing not yet implemented)"
    }