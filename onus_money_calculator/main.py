```
from .services.onus_calculator import OnusCalculatorService

def main():
    """Main entry point of the application."""
    onus_calculator_service = OnusCalculatorService()
    people = [{"name": "Alice", "share": 0.4}, {"name": "Bob", "share": 0.3}, {"name": "Charlie", "share": 0.3}]
    total_amount = 1000.0
    onus_amounts = onus_calculator_service.calculate_onus(people, total_amount)
    for person, onus_amount in onus_amounts.items():
        print(f"{person}: {onus_amount:.2f}")

if __name__ == "__main__":
    main()