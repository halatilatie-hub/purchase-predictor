def generate_recommendations(history: list[str]) -> list[dict]:
    if not history:
        return []

    return [
        {
            "product": item,
            "reason": "This item appears in the customer’s recent purchase history",
            "discount": "Special offer",
            "confidence": 0.8,
        }
        for item in history[:3]
    ]
