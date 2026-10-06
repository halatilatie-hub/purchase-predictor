from dataclasses import dataclass


@dataclass
class Product:
    id: str
    name: str
    category: str
    brand: str | None = None
    sku: str | None = None
