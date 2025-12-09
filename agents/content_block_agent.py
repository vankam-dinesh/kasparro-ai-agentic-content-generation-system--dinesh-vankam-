from dataclasses import dataclass
from typing import List, Dict, Any
from .parser_agent import ProductModel


def generate_benefits_block(product: ProductModel) -> str:
    core = ", ".join(product.benefits)
    return (
        f"This serum targets {core.lower()} while being suitable for "
        f"{', '.join(product.skin_type).lower()} skin types."
    )


def generate_usage_block(product: ProductModel) -> str:
    return (
        f"Use on clean, dry skin. {product.usage}. "
        "Avoid the eye area and always follow with sunscreen in the morning."
    )


def generate_safety_block(product: ProductModel) -> str:
    side_effects = ", ".join(product.side_effects) if product.side_effects else "no major side effects reported"
    return (
        f"Some users, especially with sensitive skin, may experience {side_effects.lower()}. "
        "Introduce the serum gradually and discontinue use if irritation persists."
    )


def generate_ingredients_block(product: ProductModel) -> str:
    return (
        f"The formula combines {', '.join(product.ingredients[:-1])} and "
        f"{product.ingredients[-1]} to balance brightening with hydration."
    )


def generate_comparison_points_block(a: ProductModel, b: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate structured comparison between Product A (model) and Product B (dict)."""
    points: List[Dict[str, Any]] = []

    points.append({
        "attribute": "Target concern",
        "product_A": "Brightening and fading dark spots.",
        "product_B": "Brightening, dark spot reduction, and added barrier support."
    })

    points.append({
        "attribute": "Skin type focus",
        "product_A": f"Designed for {', '.join(a.skin_type)} skin.",
        "product_B": b.get("skin_type_description", "Designed for normal to combination skin.")
    })

    points.append({
        "attribute": "Key ingredients",
        "product_A": ", ".join(a.ingredients),
        "product_B": ", ".join(b.get("key_ingredients", []))
    })

    points.append({
        "attribute": "Price (₹)",
        "product_A": a.price_in_inr,
        "product_B": b.get("price_in_inr")
    })

    points.append({
        "attribute": "Texture / format",
        "product_A": "Lightweight serum.",
        "product_B": b.get("texture", "Gel-cream texture.")
    })

    return points


@dataclass
class ContentBlocks:
    benefits_copy: str
    usage_copy: str
    safety_copy: str
    ingredients_copy: str


class ContentBlockAgent:
    """Agent that exposes reusable content logic blocks.

    This agent does not know about templates or pages. It simply transforms
    the structured model into reusable copy fragments.
    """

    def build_blocks_for(self, product: ProductModel) -> ContentBlocks:
        return ContentBlocks(
            benefits_copy=generate_benefits_block(product),
            usage_copy=generate_usage_block(product),
            safety_copy=generate_safety_block(product),
            ingredients_copy=generate_ingredients_block(product),
        )

    def build_comparison_points(self, product_a: ProductModel, product_b: Dict[str, Any]) -> List[Dict[str, Any]]:
        return generate_comparison_points_block(product_a, product_b)
