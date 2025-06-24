from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class Calculator_Score_EGE:
    math: Optional[int] = None
    russian_language: Optional[int] = None
    foreign_language: Optional[int] = None
    physics: Optional[int] = None
    chemistry: Optional[int] = None
    biology: Optional[int] = None
    history: Optional[int] = None
    social_studies: Optional[int] = None
    literature: Optional[int] = None
    geography: Optional[int] = None
    computer_science: Optional[int] = None
    def to_dict(self) -> Dict[str, Any]:
        return {
            "math": self.math,
            "russian_language": self.russian_language,
            "foreign_language": self.foreign_language,
            "physics": self.physics,
            "chemistry": self.chemistry,
            "biology": self.biology,
            "history": self.history,
            "social_studies": self.social_studies,
            "literature": self.literature,
            "geography": self.geography,
            "computer_science": self.computer_science
        }
    def from_dict(self, data: Dict[str, Any]) -> 'Calculator_Score_EGE':
        return Calculator_Score_EGE(
            math=data.get("math"),
            russian_language=data.get("russian_language"),
            foreign_language=data.get("foreign_language"),
            physics=data.get("physics"),
            chemistry=data.get("chemistry"),
            biology=data.get("biology"),
            history=data.get("history"),
            social_studies=data.get("social_studies"),
            literature=data.get("literature"),
            geography=data.get("geography"),
            computer_science=data.get("computer_science")
        )
    def __str__(self):
        return (f"Calculator_Score_EGE(math={self.math}, russian_language={self.russian_language}, "
                f"foreign_language={self.foreign_language}, physics={self.physics}, chemistry={self.chemistry}, "
                f"biology={self.biology}, history={self.history}, social_studies={self.social_studies}, "
                f"literature={self.literature}, geography={self.geography}, computer_science={self.computer_science})")
    def __repr__(self):
        return (f"Calculator_Score_EGE(math={self.math!r}, russian_language={self.russian_language!r}, "
                f"foreign_language={self.foreign_language!r}, physics={self.physics!r}, chemistry={self.chemistry!r}, "
                f"biology={self.biology!r}, history={self.history!r}, social_studies={self.social_studies!r}, "
                f"literature={self.literature!r}, geography={self.geography!r}, computer_science={self.computer_science!r})")
    def __eq__(self, other):
        if not isinstance(other, Calculator_Score_EGE):
            return NotImplemented
        return (self.math == other.math and
                self.russian_language == other.russian_language and
                self.foreign_language == other.foreign_language and
                self.physics == other.physics and
                self.chemistry == other.chemistry and
                self.biology == other.biology and
                self.history == other.history and
                self.social_studies == other.social_studies and
                self.literature == other.literature and
                self.geography == other.geography and
                self.computer_science == other.computer_science)
    def __ne__(self, other):
        if not isinstance(other, Calculator_Score_EGE):
            return NotImplemented
        return not self.__eq__(other)
    def __hash__(self):
        return hash((self.math, self.russian_language, self.foreign_language, self.physics,
                     self.chemistry, self.biology, self.history, self.social_studies,
                     self.literature, self.geography, self.computer_science))
    def is_complete(self) -> bool:
        return (self.math is not None and
                self.russian_language is not None and
                self.foreign_language is not None and
                self.physics is not None and
                self.chemistry is not None and
                self.biology is not None and
                self.history is not None and
                self.social_studies is not None and
                self.literature is not None and
                self.geography is not None and
                self.computer_science is not None)
    def is_empty(self) -> bool:
        return (self.math is None and
                self.russian_language is None and
                self.foreign_language is None and
                self.physics is None and
                self.chemistry is None and
                self.biology is None and
                self.history is None and
                self.social_studies is None and
                self.literature is None and
                self.geography is None and
                self.computer_science is None)
    def clear(self):
        self.math = None
        self.russian_language = None
        self.foreign_language = None
        self.physics = None
        self.chemistry = None
        self.biology = None
        self.history = None
        self.social_studies = None
        self.literature = None
        self.geography = None
        self.computer_science = None
    def update(self, other: 'Calculator_Score_EGE'):
        if not isinstance(other, Calculator_Score_EGE):
            raise TypeError("Expected an instance of Calculator_Score_EGE")
        self.math = other.math if other.math is not None else self.math
        self.russian_language = other.russian_language if other.russian_language is not None else self.russian_language
        self.foreign_language = other.foreign_language if other.foreign_language is not None else self.foreign_language
        self.physics = other.physics if other.physics is not None else self.physics
        self.chemistry = other.chemistry if other.chemistry is not None else self.chemistry
        self.biology = other.biology if other.biology is not None else self.biology
        self.history = other.history if other.history is not None else self.history
        self.social_studies = other.social_studies if other.social_studies is not None else self.social_studies
        self.literature = other.literature if other.literature is not None else self.literature
        self.geography = other.geography if other.geography is not None else self.geography
        self.computer_science = other.computer_science if other.computer_science is not None else self.computer_science
    

