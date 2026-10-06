def normalize_product_name(name: str) -> str:
    return " ".join(name.lower().split())


def match_product_name(product_name: str, catalog: list[str]) -> str:
    normalized_name = normalize_product_name(product_name)
    for item in catalog:
        if normalize_product_name(item) == normalized_name:
            return item
    return product_name
