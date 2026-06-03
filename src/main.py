"""
GPillT demo entry point.

Run from project root:
    python src/main.py

Demonstrates polymorphism by calling analyze() on every analyzer in a list.
"""

from analyzers import DosageAnalyzer, InteractionAnalyzer, SideEffectAnalyzer
from checker import InteractionChecker
from database import DrugDatabase
from models import Patient
from response import ResponseGenerator


def run_polymorphism_demo(question, analyzers):
    """
    Polymorphism demo: same method name (analyze), different class behavior.
    """
    print("  Polymorphism — each analyzer.analyze(question):")
    matched = None
    for analyzer in analyzers:
        result = analyzer.analyze(question)
        print(f"    {type(analyzer).__name__:22s} -> {result}")
        if result["intent"] and matched is None:
            matched = result
    return matched


def run_patient_demo(database, checker, response_gen):
    """
    Elderly polypharmacy demo: Patient stores Drug objects via add_drug().
    """
    print("=" * 70)
    print("Patient Medication Demo (Elderly Polypharmacy)")
    print("-" * 70)

    patient = Patient("Elderly Patient", 75)

    warfarin = database.search_drug("Warfarin")
    aspirin = database.search_drug("Aspirin")
    patient.add_drug(warfarin)
    patient.add_drug(aspirin)

    drug_names = [drug.name for drug in patient.current_drugs]
    print(f"Patient: {patient.name}, Age: {patient.age}")
    print(f"Current Drugs: {drug_names}")
    print()
    print("Sample interaction check for this patient's medications:")
    if len(patient.current_drugs) >= 2:
        result = checker.check_interaction(
            patient.current_drugs[0], patient.current_drugs[1]
        )
        print(response_gen.generate_interaction_response(result))
    print()


def handle_question(question, database, checker, response_gen, analyzers):
    print("=" * 70)
    print(f"QUESTION: {question}")
    print("-" * 70)

    analysis = run_polymorphism_demo(question, analyzers)
    print("-" * 70)
    print("ANSWER:")

    if not analysis or not analysis["intent"]:
        print("  Could not understand this question (no matching keywords).")
        return

    intent = analysis["intent"]
    drug_names = analysis["drug_names"]

    if intent == "interaction":
        if len(drug_names) < 2:
            print("  Need at least two drug names in the question.")
            return
        drug1 = database.search_drug(drug_names[0])
        drug2 = database.search_drug(drug_names[1])
        if not drug1 or not drug2:
            print("  One or more drugs were not found in the sample database.")
            return
        result = checker.check_interaction(drug1, drug2)
        print(response_gen.generate_interaction_response(result))

    elif intent == "side_effect":
        if not drug_names:
            print("  No drug name found in the question.")
            return
        drug = database.search_drug(drug_names[0])
        if not drug:
            print(f"  Drug '{drug_names[0]}' not found in the sample database.")
            return
        print(response_gen.generate_side_effect_response(drug))

    elif intent == "dosage":
        if not drug_names:
            print("  No drug name found in the question.")
            return
        drug = database.search_drug(drug_names[0])
        if not drug:
            print(f"  Drug '{drug_names[0]}' not found in the sample database.")
            return
        print(response_gen.generate_dosage_response(drug))


def main():
    print("=" * 70)
    print("GPillT: Inheritance and Polymorphism Demo")
    print("Educational sample only — NOT real medical advice")
    print("=" * 70)
    print()

    database = DrugDatabase()
    checker = InteractionChecker()
    response_gen = ResponseGenerator()

    # Polymorphism: treat different analyzer types uniformly via a list
    analyzers = [
        InteractionAnalyzer(database),
        SideEffectAnalyzer(database),
        DosageAnalyzer(database),
    ]

    run_patient_demo(database, checker, response_gen)

    questions = [
        "Can I take Warfarin together with Aspirin?",
        "What are the side effects of Norvasc?",
        "What is the dosage of VitaminC?",
    ]

    for question in questions:
        handle_question(question, database, checker, response_gen, analyzers)
        print()

    print("=" * 70)
    print("Demo complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
