from fastapi import APIRouter

router = APIRouter()


@router.get("/recommendations")
def get_recommendations():
    return [
        {
            "product": "Milk",
            "reason": "Frequently purchased in your recent orders",
            "discount": "10% off",
            "confidence": 0.92,
        },
        {
            "product": "Bread",
            "reason": "Often bought together with milk",
            "discount": "Bundle offer",
            "confidence": 0.84,
        },
    ]
