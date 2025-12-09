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

#️⃣ 1. Problem Statement (From the Assignment)

Kasparro requires building a multi-agent content system capable of:

Parsing a skincare product dataset

Generating categorized user questions

Using reusable content logic blocks

Applying structured templates

Generating 3 complete JSON pages

Running through a clear automation pipeline / DAG

Using modular agents with single responsibility

Providing clear documentation & system design

The system must NOT be:

A GPT wrapper

A prompting assignment

A single function script

A UI/website project

It is a systems engineering challenge, evaluating clarity of abstraction, modularity, orchestration, content logic, and JSON output structure.

#️⃣ 2. Solution Overview

This repository implements a production-style agentic system consisting of 5 independent agents and a DAG-style orchestrator:

✔ ProductDataParserAgent

Parses product.json → produces a clean internal ProductModel.

✔ QuestionGeneratorAgent

Generates 15+ categorized user questions (informational, usage, safety, purchase, comparison).

✔ ContentBlockAgent

Creates reusable content logic blocks:

Benefits block

Usage block

Safety block

Ingredients block

Comparison points block

These blocks are not templates — they are pure data transformation utilities.

✔ TemplateEngineAgent

Maps data + logic blocks → structured JSON pages using self-defined templates.

✔ PageAssemblyOrchestrator

DAG runner that orchestrates agents step-by-step and writes output JSON files.

#️⃣ 3. Repository Structure (Required Format)
kasparro-agentic-dinesh-vankam/
│
├── agents/
│   ├── parser_agent.py
│   ├── question_agent.py
│   ├── content_block_agent.py
│   ├── template_engine_agent.py
│
├── orchestrator/
│   └── dag_orchestrator.py
│
├── templates/
│   ├── faq_template.json
│   ├── product_template.json
│   └── comparison_template.json
│
├── data/
│   └── product.json
│
├── output/
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── docs/
│   └── projectdocumentation.md
│
├── README.md
└── main.py

#️⃣ 4. System Design (Most Important Section)

Kasparro evaluates system design more than code, so this section explains the architecture clearly.

🎯 Single Responsibility Agents
1. ProductDataParserAgent

Validates & normalizes raw product dataset

Converts to internal ProductModel dataclass

Ensures predictable typing for all downstream agents

2. QuestionGeneratorAgent

Generates 15+ categorized user questions

Categories:

Informational

Usage

Safety

Purchase

Comparison

Produces structured Q&A objects

3. ContentBlockAgent

Provides reusable, declarative content logic blocks:

Logic Block	Purpose
benefits_block	Converts benefits list → descriptive statement
usage_block	Creates structured usage guidance
safety_block	Converts side effects → safety guidance
ingredients_block	Generates highlight paragraph
comparison_block	Creates structured comparison attributes

These blocks are template-agnostic and reusable across pages.

4. TemplateEngineAgent

Works as a structured JSON template engine:

Creates:

FAQ JSON page

Product description JSON page

Comparison JSON page

Templates define:

Required fields

JSON structure

Mapping rules

5. PageAssemblyOrchestrator

Implements the automation pipeline / DAG:

product.json
     ↓
ParserAgent
     ↓
QuestionGeneratorAgent
     ↓
ContentBlockAgent
     ↓
TemplateEngineAgent
     ↓
Output JSON Files


Produces final pages:

/output/faq.json

/output/product_page.json

/output/comparison_page.json

#️⃣ 5. How to Run the Project
Step 1 — Install Python 3.9+

(Your version 3.14 also works)

Step 2 — Open terminal inside project folder

Example:

cd kasparro-agentic-dinesh-vankam

Step 3 — Run the orchestrator
python main.py

Step 4 — View generated JSON pages:
output/faq.json
output/product_page.json
output/comparison_page.json

#️⃣ 6. Templates (Defined Structure)

Each page is generated based on a structured template.

FAQ Template
{
  "product_name": "",
  "questions": [
      { "category": "", "question": "", "answer": "" }
  ]
}

Product Page Template
{
  "product_name": "",
  "short_description": "",
  "ingredients_highlight": "",
  "benefits_overview": "",
  "detailed_usage": "",
  "safety_notes": "",
  "raw": { ... }
}

Comparison Page Template
{
  "product_A": { ... },
  "product_B": { ... },
  "comparison_points": [ ... ]
}

#️⃣ 7. Output Example (Machine-Readable JSON)
Example snippet from product_page.json:
{
  "product_name": "GlowBoost Vitamin C Serum",
  "short_description": "GlowBoost Vitamin C Serum is a 10% Vitamin C serum formulated for oily, combination skin.",
  "ingredients_highlight": "The formula combines Vitamin C and Hyaluronic Acid.",
  "benefits_overview": "This serum targets brightening, fades dark spots...",
  "detailed_usage": "Use on clean, dry skin. Apply 2–3 drops...",
  "safety_notes": "Some users may experience mild tingling..."
}

#️⃣ 8. Scopes & Assumptions

Only the provided product dataset is used

No external API calls

Product B is fictional but structured

All generation is deterministic, rule-based

Focus is on system design, not creative writing

#️⃣ 9. Why This System Meets Kasparro Requirements
Requirement	Status
Multi-agent system	✔ Implemented (5 agents)
Reusable logic blocks	✔ Fully isolated blocks
Template engine	✔ JSON-based structured templates
Automation flow / DAG	✔ Orchestrator handles full pipeline
≥15 questions	✔ Included
Comparison page	✔ Included with fictional Product B
Machine-readable JSON	✔ All outputs follow strict JSON schema
Documentation	✔ Provided in README + docs/projectdocumentation.md
#️⃣ 10. Author

Dinesh Vankam
Applied AI Engineer Assignment — Kasparro
GitHub: https://github.com/vankam-dinesh

## Extensibility

- New agents can be added without modifying the existing ones, as long as inputs/outputs remain explicit.
- Additional products could be supported by adding more JSON files and extending the orchestrator.
- New page types can be added by creating additional templates and corresponding builder methods in `TemplateEngineAgent`.
