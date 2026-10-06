from dataclasses import dataclass


@dataclass
class Recommendation:
    product_name: str
    reason: str
    discount: str | None = None
    score: float = 0.0
