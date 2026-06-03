# GPillT: Polymorphism through Inheritance in a Medical QA System

A simplified medical question-answering system for **elderly polypharmacy** scenarios, built to demonstrate **Python object-oriented programming**—especially **inheritance** and **polymorphism**.

> **Disclaimer:** This repository is for **educational purposes only**. Drug data, interaction rules, and responses are **sample/demo logic**, not real medical advice. No external APIs are used.

---

## Overview

**Polypharmacy** means taking multiple medications at the same time. It is common among older adults who manage several chronic conditions. While each drug may be appropriate on its own, **combining medications** can increase the risk of:

- Harmful **drug–drug interactions**
- **Duplicate active ingredients**
- **Contraindicated combinations** based on a patient’s medication profile

For elderly patients, these risks are especially important because they often take many prescriptions and over-the-counter products daily. A structured system that can **identify question intent**, **look up drug information**, and **flag potential interaction risks** helps illustrate why medication safety workflows matter—even in a simplified, classroom setting.

**GPillT** (General Pill Toolkit) models this idea as a small in-memory QA pipeline: users ask questions in natural language, the system classifies intent, retrieves sample drug records, runs basic safety checks, and returns a formatted response.

---

## Project Goal

This project is an **Object-Oriented Programming assignment**, not a clinical product. Its primary goal is to show how OOP principles organize code clearly and extensibly:

| Goal | How GPillT addresses it |
|------|-------------------------|
| Model real-world entities | `Drug`, `Patient`, `SafetyResult` |
| Share behavior through inheritance | `BaseQuestionAnalyzer` → specialized analyzers |
| Vary behavior at runtime | Polymorphic `analyze()` calls |
| Separate concerns | Database, checking, analysis, and response layers |

The medical domain provides an intuitive narrative (questions about interactions, side effects, and dosage) while keeping logic **simple and explainable** in a written report or demo screenshot.

---

## OOP Concepts Demonstrated

### Inheritance

`BaseQuestionAnalyzer` is an **abstract base class** (`abc.ABC`) that defines the contract for all question analyzers. It provides shared utilities (such as extracting drug names from text) and declares `analyze()` as an abstract method.

Three **child classes** inherit from it and implement specialized behavior:

| Subclass | Purpose |
|----------|---------|
| `InteractionAnalyzer` | Detects questions about combining medications |
| `SideEffectAnalyzer` | Detects questions about side effects |
| `DosageAnalyzer` | Detects questions about dose or amount |

Inheritance avoids duplicating common logic while allowing each subclass to define its own keyword rules and intent labels.

### Polymorphism

**Polymorphism** means the same interface can behave differently depending on the actual object type. Here, every analyzer implements `analyze(question)`, but each subclass applies **different keyword matching** and returns a different `intent` when matched.

`main.py` treats all analyzers uniformly through a single list—no separate code path per class at the call site:

```python
analyzers = [
    InteractionAnalyzer(database),
    SideEffectAnalyzer(database),
    DosageAnalyzer(database),
]

for analyzer in analyzers:
    result = analyzer.analyze(question)  # polymorphic call
```

For a question like *"Can I take Warfarin together with Aspirin?"*, only `InteractionAnalyzer` returns a non-empty `intent`; the others return empty results. The **same method name** produces **class-specific behavior**—the core polymorphism demonstration.

---

## System Architecture

Processing follows a linear pipeline from user input to formatted output:

```
User Question
      ↓
Question Analyzer
      ↓
Drug Database
      ↓
Interaction Checker
      ↓
Response Generator
      ↓
Final Response
```

| Stage | Responsibility |
|-------|----------------|
| **Question Analyzer** | Classify intent (`interaction`, `side_effect`, `dosage`) and extract drug names |
| **Drug Database** | Supply sample `Drug` records (Norvasc, Warfarin, Aspirin, VitaminC) |
| **Interaction Checker** | Compare two drugs; return `SafetyResult` (`SAFE`, `CAUTION`, `DANGER`) |
| **Response Generator** | Format human-readable answers for the terminal demo |

Side-effect and dosage questions use the database and response generator directly after analysis; interaction questions additionally invoke the checker.

---

## File Structure

```
gpillt-oop-assignment/
├── README.md
└── src/
    ├── main.py
    ├── models.py
    ├── database.py
    ├── analyzers.py
    ├── checker.py
    └── response.py
```

### `src/models.py`

Defines core domain objects:

- **`Drug`** — name, ingredients, side effects, dosage info, contraindicated ingredients  
- **`Patient`** — name, age, current medications; `add_drug()` / `remove_drug()`  
- **`SafetyResult`** — status, reason, recommendation from interaction checks  

Demonstrates **encapsulation**: related data and behavior live in dedicated classes.

### `src/database.py`

**`DrugDatabase`** stores in-memory sample `Drug` instances and supports `search_drug(name)` and `get_all_drugs()`. Acts as the single source of drug facts for analyzers and checkers.

### `src/analyzers.py`

Contains the **inheritance and polymorphism** centerpiece:

- `BaseQuestionAnalyzer` (abstract parent)  
- `InteractionAnalyzer`, `SideEffectAnalyzer`, `DosageAnalyzer` (children)  

Each child **overrides** `analyze()` with keyword-based intent detection.

### `src/checker.py`

**`InteractionChecker`** implements sample safety rules:

1. **DANGER** — contraindicated ingredient in the other drug’s ingredients  
2. **CAUTION** — shared ingredients  
3. **SAFE** — no rule triggered  

Returns a **`SafetyResult`** object.

### `src/response.py`

**`ResponseGenerator`** formats results for the demo:

- `generate_interaction_response(result)`  
- `generate_side_effect_response(drug)`  
- `generate_dosage_response(drug)`  

Keeps presentation logic separate from analysis and checking.

### `src/main.py`

Entry point: runs the **elderly patient medication demo**, then three sample questions. Prints report-friendly output and explicitly demonstrates the **polymorphic analyzer loop**.

---

## Example Scenario

A **75-year-old patient** is registered in the demo with two medications:

| Medication | Role in demo |
|------------|----------------|
| **Warfarin** | Sample anticoagulant with contraindicated ingredients listed |
| **Aspirin** | Sample drug containing `salicylate` in its ingredients |

The system loads both drugs from the database into a `Patient` object, then runs an interaction check. Under the assignment’s **simplified rules**, Warfarin’s contraindicated list includes ingredients that match Aspirin’s profile, so the checker reports:

**Status: `DANGER`**

This scenario ties the project title to **elderly polypharmacy**: multiple drugs on one profile, with an automated flag before answering a natural-language question about the same pair.

---

## Example Output

```text
======================================================================
GPillT: Inheritance and Polymorphism Demo
Educational sample only — NOT real medical advice
======================================================================

======================================================================
Patient Medication Demo (Elderly Polypharmacy)
----------------------------------------------------------------------
Patient: Elderly Patient, Age: 75
Current Drugs: ['Warfarin', 'Aspirin']

Sample interaction check for this patient's medications:
[Interaction Check]
  Status: DANGER
  Reason: Warfarin lists contraindicated ingredient 'salicylate' which appears in Aspirin (sample rule).
  Recommendation: Demo: avoid taking these together. Consult a healthcare professional in real life.

======================================================================
QUESTION: Can I take Warfarin together with Aspirin?
----------------------------------------------------------------------
  Polymorphism — each analyzer.analyze(question):
    InteractionAnalyzer    -> {'intent': 'interaction', 'drug_names': ['Warfarin', 'Aspirin']}
    SideEffectAnalyzer     -> {'intent': '', 'drug_names': []}
    DosageAnalyzer         -> {'intent': '', 'drug_names': []}
----------------------------------------------------------------------
ANSWER:
[Interaction Check]
  Status: DANGER
  ...
```

The full run also includes side-effect and dosage questions (Norvasc, VitaminC). Run locally for complete output suitable for screenshots.

---

## How to Run

**Requirements:** Python 3.9+ (standard library only)

From the project root:

```bash
python src/main.py
```

---

## Learning Outcomes

After studying or running this project, you should be able to explain:

| Concept | In GPillT |
|---------|-----------|
| **Encapsulation** | `Drug`, `Patient`, and `SafetyResult` bundle data; `Patient` manages its drug list through methods |
| **Inheritance** | Specialized analyzers extend `BaseQuestionAnalyzer` and reuse shared helpers |
| **Polymorphism** | One loop calls `analyze()` on different analyzer types with different results |
| **Separation of responsibilities** | Models, storage, analysis, checking, and formatting live in separate modules |
| **Object-oriented design** | Abstract parent defines a contract; children implement it; `main.py` orchestrates without tight coupling |

---

## License & Use

Use this project for coursework, demos, and OOP learning. Do **not** rely on it for medical decisions.
