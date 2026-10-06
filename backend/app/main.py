from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import receipt_routes, recommendation_routes
from app.core.config import settings

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(receipt_routes.router, prefix="/api", tags=["receipts"])
app.include_router(recommendation_routes.router, prefix="/api", tags=["recommendations"])


@app.get("/")
def read_root():
    return {"message": "Purchase Predictor API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
