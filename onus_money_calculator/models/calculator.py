```
from .person import Person

class OnusCalculator:
    """Calculates the burden money for a group of people."""
    def __init__(self, people: list[Person]):
        self.people = people

    def calculate_onus(self, total_amount: float) -> dict[Person, float]:
        """Calculates the burden money for each person."""
        total_share = sum(person.share for person in self.people)
        onus_amounts = {}
        for person in self.people:
            onus_amount = (person.share / total_share) * total_amount
            onus_amounts[person] = onus_amount
        return onus_amounts