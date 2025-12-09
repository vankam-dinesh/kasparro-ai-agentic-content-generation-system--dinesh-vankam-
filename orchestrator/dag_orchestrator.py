import json
from pathlib import Path
from typing import Dict, Any

from agents.parser_agent import ProductDataParserAgent
from agents.question_agent import QuestionGeneratorAgent
from agents.content_block_agent import ContentBlockAgent
from agents.template_engine_agent import TemplateEngineAgent


class PageAssemblyOrchestrator:
    """Orchestrates the full multi-agent pipeline.

    Flow:
        raw JSON → ProductDataParserAgent
                 → QuestionGeneratorAgent
                 → ContentBlockAgent
                 → TemplateEngineAgent
                 → JSON page files
    """

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root
        self.data_dir = project_root / "data"
        self.output_dir = project_root / "output"

        # Agents
        self.parser_agent = ProductDataParserAgent()
        self.question_agent = QuestionGeneratorAgent()
        self.content_block_agent = ContentBlockAgent()
        self.template_engine = TemplateEngineAgent()

    def _load_product_data(self) -> Dict[str, Any]:
        product_path = self.data_dir / "product.json"
        with product_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _build_fictional_product_b(self) -> Dict[str, Any]:
        """Creates a fictional comparison product (no external data)."""
        return {
            "name": "RadiantLift C+Bright Gel",
            "concentration": "12% Vitamin C",
            "price_in_inr": 799,
            "skin_type_description": "Best suited for normal to combination skin.",
            "key_ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": [
                "Brightening",
                "Fades dark spots",
                "Supports skin barrier"
            ],
            "texture": "Lightweight gel-cream.",
        }

    def run(self) -> None:
        # 1. Parse product data
        raw_product = self._load_product_data()
        product_model = self.parser_agent.parse(raw_product)

        # 2. Generate questions
        questions = self.question_agent.generate_questions(product_model)

        # 3. Build content blocks
        blocks = self.content_block_agent.build_blocks_for(product_model)

        # 4. Build fictional Product B for comparison
        product_b = self._build_fictional_product_b()

        # 5. Build comparison points
        comparison_points = self.content_block_agent.build_comparison_points(product_model, product_b)

        # 6. Construct pages via template engine
        faq_page = self.template_engine.build_faq_page(product_model, questions)
        product_page = self.template_engine.build_product_page(product_model, blocks)
        comparison_page = self.template_engine.build_comparison_page(product_model, product_b, comparison_points)

        # 7. Persist as machine-readable JSON
        self.output_dir.mkdir(parents=True, exist_ok=True)

        (self.output_dir / "faq.json").write_text(
            json.dumps(faq_page, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        (self.output_dir / "product_page.json").write_text(
            json.dumps(product_page, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        (self.output_dir / "comparison_page.json").write_text(
            json.dumps(comparison_page, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    orchestrator = PageAssemblyOrchestrator(project_root=root)
    orchestrator.run()
