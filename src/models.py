"""
Data models for the GPillT assignment.

OOP concept - Encapsulation:
    Each class groups related data (attributes) and behavior (methods)
    into a single unit.
"""


class Drug:
    """Represents a sample drug entry (not real medical data)."""

    def __init__(
        self,
        name: str,
        ingredients: list,
        side_effects: list,
        dosage_info: str,
        contraindicated_ingredients: list,
    ):
        self.name = name
        self.ingredients = ingredients
        self.side_effects = side_effects
        self.dosage_info = dosage_info
        self.contraindicated_ingredients = contraindicated_ingredients

    def __repr__(self):
        return f"Drug(name={self.name!r})"


class Patient:
    """Represents a patient and their current medications."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.current_drugs = []

    def add_drug(self, drug: Drug):
        """Add a drug to the patient's current medication list."""
        if drug not in self.current_drugs:
            self.current_drugs.append(drug)

    def remove_drug(self, drug: Drug):
        """Remove a drug from the patient's current medication list."""
        if drug in self.current_drugs:
            self.current_drugs.remove(drug)


class SafetyResult:
    """Holds the outcome of a drug interaction safety check."""

    def __init__(self, status: str, reason: str, recommendation: str):
        # status is one of: "SAFE", "CAUTION", "DANGER"
        self.status = status
        self.reason = reason
        self.recommendation = recommendation
