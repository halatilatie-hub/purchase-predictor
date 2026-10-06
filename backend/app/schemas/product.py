from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: str
    name: str
    category: str
    brand: str | None = None
    sku: str | None = None
