# GPillT: Inheritance and Polymorphism in a Medical QA System

**GPillT** is a simplified, educational medical Q&A system for an Object-Oriented Programming assignment. It focuses on **inheritance** and **polymorphism** in Python—not on providing real medical advice.

> **Disclaimer:** All drug data and answers are **sample/demo data only**. Do not use this project for real health decisions. No external APIs are used.

---

## Project Overview

The system answers three kinds of questions using simple keyword matching:

| Question type   | Example keywords              | Handler                          |
|----------------|-------------------------------|----------------------------------|
| Drug interaction | together, with, combine     | `InteractionChecker` + response |
| Side effects   | side effect, problem          | `ResponseGenerator`              |
| Dosage         | dose, dosage, how much        | `ResponseGenerator`              |

Sample drugs in the database: **Norvasc**, **Warfarin**, **Aspirin**, **VitaminC**.

---

## OOP Concepts: Inheritance and Polymorphism

### Inheritance

`BaseQuestionAnalyzer` is an **abstract parent class** (`abc.ABC`). Three child classes extend it:

- `InteractionAnalyzer`
- `SideEffectAnalyzer`
- `DosageAnalyzer`

Children inherit shared behavior (e.g. `_extract_drug_names`) and must implement the abstract method `analyze()`.

### Polymorphism

In `main.py`, all analyzers are stored in one list. The same call `analyzer.analyze(question)` runs **different logic** depending on the actual class:

```python
analyzers = [
    InteractionAnalyzer(),
    SideEffectAnalyzer(),
    DosageAnalyzer(),
]
for analyzer in analyzers:
    result = analyzer.analyze(question)
```

The program does not need separate `if` branches for each analyzer type at the call site—that is polymorphism.

---

## File Structure

```
gpillt-oop-assignment/
├── README.md
└── src/
    ├── main.py       # Demo runner (3 sample questions)
    ├── models.py     # Drug, Patient, SafetyResult
    ├── database.py   # DrugDatabase (sample drugs)
    ├── checker.py    # InteractionChecker
    ├── analyzers.py  # Analyzer hierarchy (inheritance / polymorphism)
    └── response.py   # ResponseGenerator
```

| File            | Role |
|-----------------|------|
| `models.py`     | Core data classes |
| `database.py`   | In-memory sample drug storage |
| `checker.py`    | SAFE / CAUTION / DANGER rules |
| `analyzers.py`  | Question intent detection (main OOP demo) |
| `response.py`   | Formatted answer strings |
| `main.py`       | Runs demo and prints report-friendly output |

---

## How to Run

Requirements: **Python 3.9+** (stdlib only).

From the project root:

```bash
python src/main.py
```

---

## Example Output

```
======================================================================
GPillT: Inheritance and Polymorphism Demo
Educational sample only — NOT real medical advice
======================================================================

======================================================================
QUESTION: Can I take Warfarin together with Aspirin?
----------------------------------------------------------------------
  Polymorphism — each analyzer.analyze(question):
    InteractionAnalyzer    -> {'intent': 'interaction', 'drug_names': ['Warfarin', 'Aspirin']}
    SideEffectAnalyzer       -> {'intent': '', 'drug_names': []}
    DosageAnalyzer           -> {'intent': '', 'drug_names': []}
----------------------------------------------------------------------
ANSWER:
[Interaction Check]
  Status: DANGER
  Reason: Warfarin lists contraindicated ingredient 'salicylate' which appears in Aspirin (sample rule).
  Recommendation: Demo: avoid taking these together. Consult a healthcare professional in real life.

======================================================================
QUESTION: What are the side effects of Norvasc?
...
```

The demo also prints a **Patient Medication Demo** section: an elderly patient on Warfarin and Aspirin, illustrating polypharmacy and a sample interaction check.

Run the program locally and capture a terminal screenshot for your report.

---

## Assignment Notes

- **Encapsulation:** `Drug`, `Patient`, and `SafetyResult` bundle related fields.
- **Inheritance:** Analyzer children extend `BaseQuestionAnalyzer`.
- **Polymorphism:** One loop over `analyzers` calls `analyze()` on each type.
- **Abstraction:** `analyze()` is abstract in the parent; children supply concrete behavior.
