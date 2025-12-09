# Project Documentation – Multi-Agent Content Generation System

## Problem Statement

Design and implement a modular, agentic automation system that:

- Takes a small, structured product dataset as input.
- Automatically generates:
  - A categorized FAQ page.
  - A structured product description page.
  - A product comparison page (against a fictional Product B).
- Produces all final pages as **clean, machine-readable JSON**.
- Demonstrates:
  - Multi-agent workflows.
  - Automation / orchestration flow.
  - Reusable content logic blocks.
  - Template-based generation.
  - Clear abstractions and documentation.

## Solution Overview

The solution is implemented as a **multi-agent Python system**. Each agent has:

- A **single responsibility**.
- Explicit **inputs and outputs**.
- No hidden global state.

A top-level orchestrator coordinates these agents in a directed flow to produce three JSON pages:

1. `faq.json` – FAQ page with at least 15 categorized Q&A pairs.
2. `product_page.json` – structured representation of the product description.
3. `comparison_page.json` – comparison between the core product and a fictional Product B.

### Key Design Choices

- Internal product data is normalized into a `ProductModel` dataclass.
- **Reusable logic blocks** transform structured data into copy fragments.
- A **template engine** converts these fragments into stable JSON page structures.
- A dedicated **orchestrator** models the automation graph and persists outputs.

## Scope & Assumptions

- The system currently operates on a **single product dataset** (`GlowBoost Vitamin C Serum`).
- All logic is **deterministic** and rule-based; no external APIs or models are required.
- Product B is fictional and defined entirely within the orchestrator.
- No UI, web server, or database is included; the focus is on system design and JSON outputs.
- Error handling is minimal but sufficient for the controlled assignment environment.

## System Design

### Agents and Responsibilities

1. **ProductDataParserAgent**
   - Input: Raw dict loaded from `data/product.json`.
   - Output: `ProductModel` dataclass instance.
   - Responsibility: Validate and normalize the product data.

2. **QuestionGeneratorAgent**
   - Input: `ProductModel`.
   - Output: List of `Question` objects.
   - Responsibility: Generate at least 15 user questions and concise answers,
     categorized into Informational, Safety, Usage, Purchase, and Comparison.

3. **ContentBlockAgent**
   - Input: `ProductModel` (and Product B for comparison).
   - Output: `ContentBlocks` (benefits, usage, safety, ingredients copy) and structured comparison points.
   - Responsibility: Apply reusable content logic blocks such as:
     - `generate_benefits_block`
     - `generate_usage_block`
     - `generate_safety_block`
     - `generate_ingredients_block`
     - `generate_comparison_points_block`

4. **TemplateEngineAgent**
   - Inputs:
     - `ProductModel`
     - List of `Question`
     - `ContentBlocks`
     - Fictional Product B
     - Comparison points
   - Output:
     - FAQ page JSON
     - Product page JSON
     - Comparison page JSON
   - Responsibility: Map structured data and content blocks into template-defined JSON page structures.

5. **PageAssemblyOrchestrator**
   - Inputs: Project root path and access to all agents.
   - Output: Persisted JSON files in `output/`.
   - Responsibility:
     1. Load raw product JSON.
     2. Invoke agents in the correct sequence.
     3. Write resulting pages to disk.

### Orchestration Flow (Automation Graph)

```text
+--------------------------+
|  data/product.json       |
+------------+-------------+
             |
             v
+--------------------------+
| ProductDataParserAgent   |
+------------+-------------+
             |
             v
+--------------------------+
| QuestionGeneratorAgent   |
+------------+-------------+
             |
             v
+--------------------------+
|  ContentBlockAgent       |
+------------+-------------+
             |
             v
+--------------------------+
|  TemplateEngineAgent     |
+------------+-------------+
             |
             v
+--------------------------+
| PageAssemblyOrchestrator |
+------------+-------------+
             |
             v
+--------------------------+
|   JSON Outputs (FAQ,     |
|   Product, Comparison)   |
+--------------------------+
```

This flow behaves like a simple DAG where each agent consumes the output of the previous one and enriches the state for the next stage.

### Content Logic Blocks

The following reusable content logic blocks are defined:

- `generate_benefits_block(product)`
  - Builds a short paragraph describing the key benefits and suitable skin types.
- `generate_usage_block(product)`
  - Produces a structured usage description, including routine context and warnings.
- `generate_safety_block(product)`
  - Converts side effects into human-readable safety notes.
- `generate_ingredients_block(product)`
  - Summarizes the role of the key ingredients.
- `generate_comparison_points_block(product_a, product_b)`
  - Produces a list of structured comparison points with an `attribute`, `product_A`, and `product_B` value.

These blocks are **agnostic of templates** and can be reused for multiple page types.

### Template System

Templates are expressed as **JSON structures** that define:

- Required fields (e.g., `product_name`, `questions`, `comparison_points`).
- How content blocks are mapped to those fields.

The actual filling is implemented in `TemplateEngineAgent`:

- `build_faq_page(product, questions)`
- `build_product_page(product, blocks)`
- `build_comparison_page(product_a, product_b, comparison_points)`

This keeps templates declarative and the mapping logic centralized.

## Future Extensions

- Add multiple products and dynamic selection of which product(s) to process.
- Introduce configuration-driven templates so non-engineers can adjust field layouts.
- Integrate an LLM-based agent for more varied language while keeping the overall architecture unchanged.

---

This documentation focuses on the **system design perspective**, as required by the assignment, rather than per-file walkthroughs.
