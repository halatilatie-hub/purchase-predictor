from pydantic import BaseModel


class RecommendationSchema(BaseModel):
    product_name: str
    reason: str
    discount: str | None = None
    score: float = 0.0
