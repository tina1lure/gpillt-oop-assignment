# GPillT: An Object-Oriented Medical QA System for Elderly Polypharmacy Medication Safety

GPillT, short for **General Pill Toolkit**, is a simplified medical question-answering system designed for elderly polypharmacy scenarios. This project was implemented as an Object-Oriented Programming assignment related to my future interest in healthcare AI, biomedical AI systems, and medication safety support.

The system models a small medication QA workflow using object-oriented design. It receives medication-related questions, analyzes the question type, retrieves sample drug information, checks simplified drug interaction rules, and prints a readable response.

**Disclaimer:** This repository is for educational purposes only. Drug data, interaction rules, and responses are sample/demo logic, not real medical advice. No external APIs, real medical databases, or real patient records are used.

---

## Report

The final assignment report is available here:

[Download GPillT OOP Report](docs/GPillT_OOP_Report.pdf)

---

## Overview

Polypharmacy means taking multiple medications at the same time. It is common among older adults who manage several chronic conditions. While each drug may be appropriate on its own, combining medications can increase the risk of:

* Harmful drug-drug interactions
* Duplicate active ingredients
* Contraindicated combinations
* Confusing dosage or safety information

For elderly patients, these risks are especially important because they often take several prescriptions and over-the-counter products daily.

GPillT models this scenario as a small object-oriented medical QA pipeline:

```text
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

The project focuses on designing a clear OOP architecture rather than building a real clinical system.

---

## Project Goal

The goal of this project is to practically implement an object-oriented system related to healthcare AI and medication safety.

GPillT demonstrates how object-oriented programming can be used to organize a medical QA system into meaningful classes and modules.

| Goal                             | How GPillT Addresses It                                       |
| -------------------------------- | ------------------------------------------------------------- |
| Model real-world entities        | `Drug`, `Patient`, `SafetyResult`                             |
| Separate system responsibilities | `DrugDatabase`, `InteractionChecker`, `ResponseGenerator`     |
| Handle different question types  | `InteractionAnalyzer`, `SideEffectAnalyzer`, `DosageAnalyzer` |
| Support extensibility            | New analyzer classes can be added later                       |
| Connect OOP with healthcare AI   | Medication QA workflow is modeled as an OOP system            |

---

## Main Features

GPillT supports three simplified medication QA tasks.

1. **Drug Interaction Question**

   * Example: `Can I take Warfarin together with Aspirin?`
   * The system detects an interaction question, retrieves two drug records, checks simplified interaction rules, and returns a safety result.

2. **Side Effect Question**

   * Example: `What are the side effects of Norvasc?`
   * The system detects a side-effect question and returns sample side-effect information.

3. **Dosage Question**

   * Example: `What is the dosage of VitaminC?`
   * The system detects a dosage question and returns sample dosage information.

The system also includes an elderly patient medication demo using a 75-year-old patient taking Warfarin and Aspirin.

---

## OOP Design

### 1. Encapsulation

The system groups related data and behavior into classes.

* `Drug` stores drug name, ingredients, side effects, dosage information, and contraindicated ingredients.
* `Patient` stores patient name, age, and the current medication list.
* `SafetyResult` stores the result of an interaction check.

This makes the code easier to understand because each object represents a meaningful concept in the medication QA workflow.

---

### 2. Separation of Responsibilities

Each module has a clear role.

| File           | Responsibility                           |
| -------------- | ---------------------------------------- |
| `models.py`    | Defines core domain objects              |
| `database.py`  | Stores and retrieves sample drug data    |
| `analyzers.py` | Analyzes user questions                  |
| `checker.py`   | Checks simplified drug interaction rules |
| `response.py`  | Formats readable output                  |
| `main.py`      | Runs the full demo                       |

This structure avoids placing all logic in one file and makes the system easier to extend.

---

### 3. Inheritance and Polymorphism

The question analyzers demonstrate inheritance and polymorphism.

`BaseQuestionAnalyzer` is an abstract parent class. Three child classes inherit from it:

```text
BaseQuestionAnalyzer
 ├── InteractionAnalyzer
 ├── SideEffectAnalyzer
 └── DosageAnalyzer
```

Each analyzer implements the same method:

```python
analyze(question)
```

However, each class behaves differently depending on the question type.

In `main.py`, all analyzers are handled through one common loop:

```python
analyzers = [
    InteractionAnalyzer(database),
    SideEffectAnalyzer(database),
    DosageAnalyzer(database),
]

for analyzer in analyzers:
    result = analyzer.analyze(question)
```

This means the same method call can produce different results depending on the object type. This is the main polymorphism example in the project.

---

## System Architecture

The system follows a simple pipeline.

| Stage               | Responsibility                            |
| ------------------- | ----------------------------------------- |
| Question Analyzer   | Classifies intent and extracts drug names |
| Drug Database       | Supplies sample `Drug` objects            |
| Interaction Checker | Compares drugs and returns `SafetyResult` |
| Response Generator  | Formats final terminal responses          |

Interaction questions use the full pipeline. Side-effect and dosage questions use the database and response generator after question analysis.

---

## File Structure

```text
gpillt-oop-assignment/
├── README.md
├── docs/
│   └── GPillT_OOP_Report.pdf
└── src/
    ├── main.py
    ├── models.py
    ├── database.py
    ├── analyzers.py
    ├── checker.py
    └── response.py
```

---

## Class Summary

### `Drug`

Represents a medication.

Main attributes:

* `name`
* `ingredients`
* `side_effects`
* `dosage_info`
* `contraindicated_ingredients`

---

### `Patient`

Represents an elderly patient in the polypharmacy demo.

Main attributes and methods:

* `name`
* `age`
* `current_drugs`
* `add_drug()`
* `remove_drug()`

---

### `SafetyResult`

Stores the result of a medication safety check.

Main attributes:

* `status`
* `reason`
* `recommendation`

Possible statuses:

* `SAFE`
* `CAUTION`
* `DANGER`

---

### `DrugDatabase`

Stores in-memory sample drug records.

Sample drugs:

* `Norvasc`
* `Warfarin`
* `Aspirin`
* `VitaminC`

Main methods:

* `search_drug(name)`
* `get_all_drugs()`

---

### `InteractionChecker`

Checks simplified interaction rules.

Rules:

* `DANGER`: one drug's contraindicated ingredient appears in the other drug's ingredients
* `CAUTION`: two drugs share ingredients
* `SAFE`: no sample rule is triggered

---

### `ResponseGenerator`

Formats the output for interaction, side-effect, and dosage responses.

Main methods:

* `generate_interaction_response(result)`
* `generate_side_effect_response(drug)`
* `generate_dosage_response(drug)`

---

## Example Scenario

A 75-year-old patient is registered in the demo with two medications:

| Medication | Role in Demo                                 |
| ---------- | -------------------------------------------- |
| Warfarin   | Sample drug with contraindicated ingredients |
| Aspirin    | Sample drug containing salicylate            |

The system loads both drugs from the database into a `Patient` object, then runs an interaction check.

Under the simplified demo rule, Warfarin lists `salicylate` as a contraindicated ingredient, and Aspirin contains `salicylate`. Therefore, the checker reports:

```text
Status: DANGER
```

This scenario connects the OOP system to elderly polypharmacy medication safety.

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
  Reason: Warfarin lists contraindicated ingredient 'salicylate' which appears in Aspirin (sample rule).
  Recommendation: Demo: avoid taking these together. Consult a healthcare professional in real life.
```

The full run also includes:

* Side-effect question for `Norvasc`
* Dosage question for `VitaminC`

---

## How to Run

Requirements:

```text
Python 3.9+
Standard library only
```

Run the project from the repository root:

```bash
python src/main.py
```

No external package installation is required.

---

## Learning Outcomes

Through this project, I practiced the following OOP concepts:

| Concept                        | In GPillT                                                           |
| ------------------------------ | ------------------------------------------------------------------- |
| Encapsulation                  | `Drug`, `Patient`, and `SafetyResult` bundle related data           |
| Abstraction                    | The system hides internal checking logic behind clear class methods |
| Inheritance                    | Specialized analyzers extend `BaseQuestionAnalyzer`                 |
| Polymorphism                   | One loop calls `analyze()` on different analyzer types              |
| Separation of Responsibilities | Database, analysis, checking, and response logic are separated      |
| Extensibility                  | New question types can be added with new analyzer classes           |

---

## Limitations

GPillT is an educational demo and has several limitations.

* The drug database contains only four sample drugs.
* The interaction rules are simplified.
* Question analysis is keyword-based.
* The system runs only in the terminal.
* There is no real medical database, real patient data, or expert verification.

A future version could connect to a validated drug database, use NLP or LLM-based question analysis, store patient medication history, and provide a web or mobile interface.

---

## License & Use

This project is for coursework, demos, and OOP learning.

Do not rely on it for real medical decisions.
