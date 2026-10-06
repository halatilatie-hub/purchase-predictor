from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ReceiptItem:
    product_name: str
    quantity: int = 1
    unit_price: float = 0.0
    total: float = 0.0


@dataclass
class Receipt:
    id: str
    customer_id: str
    purchase_date: datetime
    total_amount: float
    items: list[ReceiptItem] = field(default_factory=list)
