from dataclasses import asdict
from typing import Any, Dict, List
from .parser_agent import ProductModel
from .question_agent import Question
from .content_block_agent import ContentBlocks


class TemplateEngineAgent:
    """Agent that applies templates to content blocks and product data.

    The 'templates' in this system are JSON-like structures that define fields
    and their composition rules. This agent is responsible for mapping:

        data (ProductModel + ContentBlocks + Questions + ProductB)
        → structured JSON pages
    """

    def build_faq_page(self, product: ProductModel, questions: List[Question]) -> Dict[str, Any]:
        return {
            "product_name": product.name,
            "questions": [
                {
                    "category": q.category,
                    "question": q.question,
                    "answer": q.answer,
                }
                for q in questions
            ],
        }

    def build_product_page(self, product: ProductModel, blocks: ContentBlocks) -> Dict[str, Any]:
        return {
            "product_name": product.name,
            "short_description": (
                f"{product.name} is a {product.concentration} serum formulated for "
                f"{', '.join(product.skin_type).lower()} skin."
            ),
            "ingredients_highlight": blocks.ingredients_copy,
            "benefits_overview": blocks.benefits_copy,
            "detailed_usage": blocks.usage_copy,
            "safety_notes": blocks.safety_copy,
            "raw": {
                "concentration": product.concentration,
                "skin_type": product.skin_type,
                "ingredients": product.ingredients,
                "benefits": product.benefits,
                "usage": product.usage,
                "side_effects": product.side_effects,
                "price_in_inr": product.price_in_inr,
            },
        }

    def build_comparison_page(
        self,
        product_a: ProductModel,
        product_b: Dict[str, Any],
        comparison_points: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        return {
            "product_A": {
                "name": product_a.name,
                "concentration": product_a.concentration,
                "price_in_inr": product_a.price_in_inr,
                "skin_type": product_a.skin_type,
                "key_ingredients": product_a.ingredients,
                "benefits": product_a.benefits,
            },
            "product_B": product_b,
            "comparison_points": comparison_points,
        }
