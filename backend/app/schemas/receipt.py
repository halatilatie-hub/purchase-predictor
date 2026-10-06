from datetime import datetime

from pydantic import BaseModel


class ReceiptItemSchema(BaseModel):
    product_name: str
    quantity: int = 1
    unit_price: float = 0.0
    total: float = 0.0


class ReceiptSchema(BaseModel):
    id: str
    customer_id: str
    purchase_date: datetime
    total_amount: float
    items: list[ReceiptItemSchema]
