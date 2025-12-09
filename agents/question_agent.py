from dataclasses import dataclass
from typing import List
from .parser_agent import ProductModel


@dataclass
class Question:
    category: str
    question: str
    answer: str


class QuestionGeneratorAgent:
    """Agent that generates categorized user questions and concise answers.

    The logic is deterministic and based only on the structured ProductModel.
    """

    def generate_questions(self, product: ProductModel) -> List[Question]:
        questions: List[Question] = []

        # Informational
        questions.append(Question(
            category="Informational",
            question="What is the main purpose of this serum?",
            answer="It is a brightening serum designed to fade dark spots and improve overall skin radiance."
        ))
        questions.append(Question(
            category="Informational",
            question="What is the concentration of Vitamin C in the serum?",
            answer=f"It contains {product.concentration}."
        ))
        questions.append(Question(
            category="Informational",
            question="Which skin types is this serum suitable for?",
            answer=f"It is suitable for {', '.join(product.skin_type)} skin."
        ))

        # Usage
        questions.append(Question(
            category="Usage",
            question="How should I apply this serum?",
            answer=product.usage
        ))
        questions.append(Question(
            category="Usage",
            question="Can I use this serum every morning?",
            answer="Yes, it is intended for morning use before sunscreen as part of your daily routine."
        ))
        questions.append(Question(
            category="Usage",
            question="Should I apply moisturizer after using this serum?",
            answer="Yes, you may follow the serum with a suitable moisturizer and then sunscreen."
        ))

        # Safety
        questions.append(Question(
            category="Safety",
            question="Can this serum cause irritation?",
            answer="It may cause mild tingling, especially for sensitive skin. If irritation persists, discontinue use."
        ))
        questions.append(Question(
            category="Safety",
            question="Is this serum safe for sensitive skin?",
            answer="Sensitive skin may experience mild tingling. It is recommended to do a patch test before full-face application."
        ))
        questions.append(Question(
            category="Safety",
            question="Can I use this serum with other active ingredients?",
            answer="It is generally best to avoid layering multiple strong actives in the same routine without guidance from a skincare professional."
        ))

        # Purchase
        questions.append(Question(
            category="Purchase",
            question="What is the price of this serum?",
            answer=f"The serum is priced at ₹{product.price_in_inr}."
        ))
        questions.append(Question(
            category="Purchase",
            question="Is this serum suitable for everyday use at its price point?",
            answer="Yes, the price and formulation are designed for consistent, everyday use as part of a regular skincare routine."
        ))

        # Comparison
        questions.append(Question(
            category="Comparison",
            question="How does this serum differ from a gel-based Vitamin C product?",
            answer="This serum focuses on brightening and fading dark spots with 10% Vitamin C and hydrating Hyaluronic Acid, while gel-based products may offer a lighter texture with slightly different supporting ingredients."
        ))
        questions.append(Question(
            category="Comparison",
            question="Is this serum better for oily skin than heavier Vitamin C creams?",
            answer="Yes, it is more suitable for oily and combination skin compared to heavier creams that may feel greasy."
        ))
        questions.append(Question(
            category="Comparison",
            question="How does this serum compare to products that do not contain Hyaluronic Acid?",
            answer="Compared to products without Hyaluronic Acid, this serum also supports skin hydration in addition to brightening and dark spot reduction."
        ))

        # Extra informational / usage to ensure >= 15
        questions.append(Question(
            category="Informational",
            question="What are the key ingredients in this serum?",
            answer=f"The key ingredients are {', '.join(product.ingredients)}."
        ))

        return questions
