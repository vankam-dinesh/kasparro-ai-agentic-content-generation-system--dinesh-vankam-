# Kasparro – Agentic Content Generation System

This repository implements a modular, multi-agent content generation system for a single skincare product.
The system takes a small, structured product dataset and produces three machine-readable JSON pages:

- `faq.json` – categorized FAQ page
- `product_page.json` – structured product description page
- `comparison_page.json` – comparison between the primary product and a fictional Product B

## Architecture Overview

The system is intentionally **not** a monolithic script. It is composed of:

- **ProductDataParserAgent** – parses `data/product.json` into an internal `ProductModel`.
- **QuestionGeneratorAgent** – generates categorized user questions and deterministic answers.
- **ContentBlockAgent** – exposes reusable content logic blocks (benefits, usage, safety, ingredients, comparison).
- **TemplateEngineAgent** – converts data + content blocks into JSON pages based on template structures.
- **PageAssemblyOrchestrator** – orchestrates the agents in a DAG-like flow and writes final JSON outputs.

All final outputs are pure JSON and can be consumed directly by downstream systems.

## Project Structure

```text
.
├── agents/
│   ├── parser_agent.py
│   ├── question_agent.py
│   ├── content_block_agent.py
│   └── template_engine_agent.py
├── orchestrator/
│   └── dag_orchestrator.py
├── templates/
│   ├── faq_template.json
│   ├── product_template.json
│   └── comparison_template.json
├── data/
│   └── product.json
├── output/
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
├── docs/
│   └── projectdocumentation.md
├── main.py
└── README.md
```

## Running the Pipeline

1. Ensure you have Python 3.9+ installed.
2. From the project root directory, run:

```bash
python main.py
```

This will generate the three JSON pages inside the `output/` folder.

## Extensibility

- New agents can be added without modifying the existing ones, as long as inputs/outputs remain explicit.
- Additional products could be supported by adding more JSON files and extending the orchestrator.
- New page types can be added by creating additional templates and corresponding builder methods in `TemplateEngineAgent`.
