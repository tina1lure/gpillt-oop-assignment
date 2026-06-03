"""
Sample drug database (educational data only — not real medical advice).
"""

from models import Drug


class DrugDatabase:
    """Stores sample Drug objects and provides lookup methods."""

    def __init__(self):
        # Sample drugs for the assignment (fictional / simplified data)
        self._drugs = {
            "norvasc": Drug(
                name="Norvasc",
                ingredients=["amlodipine"],
                side_effects=["dizziness (sample)", "swelling (sample)"],
                dosage_info="5 mg once daily (sample only)",
                contraindicated_ingredients=[],
            ),
            "warfarin": Drug(
                name="Warfarin",
                ingredients=["warfarin"],
                side_effects=["bleeding risk (sample)", "bruising (sample)"],
                dosage_info="As prescribed by doctor (sample only)",
                contraindicated_ingredients=["salicylate", "aspirin"],
            ),
            "aspirin": Drug(
                name="Aspirin",
                ingredients=["acetylsalicylic acid", "salicylate"],
                side_effects=["stomach upset (sample)", "bleeding (sample)"],
                dosage_info="100 mg once daily (sample only)",
                contraindicated_ingredients=[],
            ),
            "vitaminc": Drug(
                name="VitaminC",
                ingredients=["ascorbic acid"],
                side_effects=["stomach pain at high dose (sample)"],
                dosage_info="500 mg once daily (sample only)",
                contraindicated_ingredients=[],
            ),
        }

    def search_drug(self, name: str):
        """Return a Drug by name, or None if not found."""
        key = name.strip().lower().replace(" ", "")
        return self._drugs.get(key)

    def get_all_drugs(self):
        """Return a list of all sample drugs in the database."""
        return list(self._drugs.values())
