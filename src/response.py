"""
Formats answers for the demo QA system.
"""

from models import Drug, SafetyResult


class ResponseGenerator:
    """Builds human-readable response strings from check results and drugs."""

    def generate_interaction_response(self, result: SafetyResult) -> str:
        return (
            "[Interaction Check]\n"
            f"  Status: {result.status}\n"
            f"  Reason: {result.reason}\n"
            f"  Recommendation: {result.recommendation}"
        )

    def generate_side_effect_response(self, drug: Drug) -> str:
        if drug.side_effects:
            effects = ", ".join(drug.side_effects)
        else:
            effects = "none listed (sample)"
        return (
            "[Side Effects]\n"
            f"  Drug: {drug.name}\n"
            f"  Sample side effects: {effects}\n"
            "  Note: Educational sample data only — not real medical advice."
        )

    def generate_dosage_response(self, drug: Drug) -> str:
        return (
            "[Dosage Info]\n"
            f"  Drug: {drug.name}\n"
            f"  Sample dosage: {drug.dosage_info}\n"
            "  Note: Educational sample data only — not real medical advice."
        )
