from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class ProductModel:
    name: str
    concentration: str
    skin_type: List[str]
    ingredients: List[str]
    benefits: List[str]
    usage: str
    side_effects: List[str]
    price_in_inr: int


class ProductDataParserAgent:
    """Agent responsible for parsing raw product JSON into a strongly typed internal model.

    Responsibilities:
    - Validate expected keys
    - Normalize field names
    - Provide a clean internal representation (ProductModel)
    """

    REQUIRED_KEYS = [
        "product_name",
        "concentration",
        "skin_type",
        "key_ingredients",
        "benefits",
        "how_to_use",
        "side_effects",
        "price_in_inr",
    ]

    def parse(self, raw: Dict[str, Any]) -> ProductModel:
        missing = [k for k in self.REQUIRED_KEYS if k not in raw]
        if missing:
            raise ValueError(f"Missing required keys in product data: {missing}")

        # Normalize side effects to list
        side_effects_raw = raw.get("side_effects", "")
        if isinstance(side_effects_raw, str):
            side_effects = [s.strip() for s in side_effects_raw.split(",") if s.strip()]
        else:
            side_effects = list(side_effects_raw)

        return ProductModel(
            name=raw["product_name"],
            concentration=raw["concentration"],
            skin_type=list(raw["skin_type"]),
            ingredients=list(raw["key_ingredients"]),
            benefits=list(raw["benefits"]),
            usage=raw["how_to_use"],
            side_effects=side_effects,
            price_in_inr=int(raw["price_in_inr"]),
        )
