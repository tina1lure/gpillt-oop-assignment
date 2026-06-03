"""
Question analyzers — main inheritance and polymorphism demo.

OOP concept - Inheritance:
    Child classes (InteractionAnalyzer, SideEffectAnalyzer, DosageAnalyzer)
    inherit from BaseQuestionAnalyzer and reuse shared helpers.

OOP concept - Polymorphism:
    Each child overrides analyze() with different behavior.
    Code can call analyzer.analyze(question) without knowing the exact type.
"""

from abc import ABC, abstractmethod

from database import DrugDatabase


class BaseQuestionAnalyzer(ABC):
    """
    Abstract parent class.
    Subclasses MUST implement analyze() — enforced by @abstractmethod.
    """

    def __init__(self, database=None):
        self.database = database if database is not None else DrugDatabase()

    @abstractmethod
    def analyze(self, question: str) -> dict:
        """Return {"intent": str, "drug_names": list}."""
        pass

    def _extract_drug_names(self, question: str) -> list:
        """Find drug names from the question using the sample database."""
        question_lower = question.lower()
        found = []
        for drug in self.database.get_all_drugs():
            if drug.name.lower() in question_lower:
                found.append(drug.name)
        return found


class InteractionAnalyzer(BaseQuestionAnalyzer):
    """Detects questions about taking drugs together."""

    KEYWORDS = ("together", "with", "combine")

    def analyze(self, question: str) -> dict:
        question_lower = question.lower()
        if not any(keyword in question_lower for keyword in self.KEYWORDS):
            return {"intent": "", "drug_names": []}
        return {
            "intent": "interaction",
            "drug_names": self._extract_drug_names(question),
        }


class SideEffectAnalyzer(BaseQuestionAnalyzer):
    """Detects questions about side effects."""

    KEYWORDS = ("side effect", "problem")

    def analyze(self, question: str) -> dict:
        question_lower = question.lower()
        if not any(keyword in question_lower for keyword in self.KEYWORDS):
            return {"intent": "", "drug_names": []}
        return {
            "intent": "side_effect",
            "drug_names": self._extract_drug_names(question),
        }


class DosageAnalyzer(BaseQuestionAnalyzer):
    """Detects questions about dosage."""

    KEYWORDS = ("dose", "dosage", "how much")

    def analyze(self, question: str) -> dict:
        question_lower = question.lower()
        if not any(keyword in question_lower for keyword in self.KEYWORDS):
            return {"intent": "", "drug_names": []}
        return {
            "intent": "dosage",
            "drug_names": self._extract_drug_names(question),
        }
