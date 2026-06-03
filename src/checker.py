"""
Drug interaction checker using simple sample rules.
"""

from models import Drug, SafetyResult


class InteractionChecker:
    """Checks pairs of drugs and returns a SafetyResult."""

    def check_interaction(self, drug1: Drug, drug2: Drug) -> SafetyResult:
        """
        Run all checks in priority order:
        1) contraindications -> DANGER
        2) duplicate ingredients -> CAUTION
        3) otherwise -> SAFE
        """
        result = self.check_contraindications(drug1, drug2)
        if result.status == "DANGER":
            return result

        result = self.check_duplicate_ingredients(drug1, drug2)
        if result.status == "CAUTION":
            return result

        return SafetyResult(
            status="SAFE",
            reason=(
                f"No sample-rule interaction found between "
                f"{drug1.name} and {drug2.name}."
            ),
            recommendation=(
                "This is assignment demo data only. "
                "Do not use for real medical decisions."
            ),
        )

    def check_contraindications(self, drug1: Drug, drug2: Drug) -> SafetyResult:
        """DANGER if a contraindicated ingredient appears in the other drug."""
        for banned in drug1.contraindicated_ingredients:
            if self._ingredient_in_drug(banned, drug2):
                return SafetyResult(
                    status="DANGER",
                    reason=(
                        f"{drug1.name} lists contraindicated ingredient "
                        f"'{banned}' which appears in {drug2.name} (sample rule)."
                    ),
                    recommendation=(
                        "Demo: avoid taking these together. "
                        "Consult a healthcare professional in real life."
                    ),
                )

        for banned in drug2.contraindicated_ingredients:
            if self._ingredient_in_drug(banned, drug1):
                return SafetyResult(
                    status="DANGER",
                    reason=(
                        f"{drug2.name} lists contraindicated ingredient "
                        f"'{banned}' which appears in {drug1.name} (sample rule)."
                    ),
                    recommendation=(
                        "Demo: avoid taking these together. "
                        "Consult a healthcare professional in real life."
                    ),
                )

        return SafetyResult(status="SAFE", reason="", recommendation="")

    def check_duplicate_ingredients(self, drug1: Drug, drug2: Drug) -> SafetyResult:
        """CAUTION if both drugs share at least one ingredient."""
        set1 = {ing.lower() for ing in drug1.ingredients}
        set2 = {ing.lower() for ing in drug2.ingredients}
        shared = set1 & set2

        if shared:
            shared_str = ", ".join(sorted(shared))
            return SafetyResult(
                status="CAUTION",
                reason=f"Shared ingredients (sample): {shared_str}.",
                recommendation="Demo: watch for duplicate-ingredient overlap.",
            )

        return SafetyResult(status="SAFE", reason="", recommendation="")

    @staticmethod
    def _ingredient_in_drug(ingredient: str, drug: Drug) -> bool:
        """True if ingredient string matches any entry in drug.ingredients."""
        needle = ingredient.lower()
        return any(needle in ing.lower() for ing in drug.ingredients)
