from app.models.receipt import Receipt, ReceiptItem


def parse_receipt_lines(lines: list[str]) -> Receipt:
    """Convert raw OCR lines into a structured receipt object."""
    parsed_items = [ReceiptItem(product_name=line, quantity=1, unit_price=0.0, total=0.0) for line in lines]
    return Receipt(
        id="receipt-001",
        customer_id="customer-001",
        purchase_date=None,
        total_amount=0.0,
        items=parsed_items,
    )
