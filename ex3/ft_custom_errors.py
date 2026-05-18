
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)

def test_specific_errors() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

def test_catch_all() -> None:
    print("Testing catching all garden errors...")
    for err in [PlantError("The tomato plant is wilting!"),
                WaterError("Not enough water in the tank!")]:
        try:
            raise err
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print()

def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    test_specific_errors()
    test_catch_all()
    print("All custom error types work correctly!")

if __name__ == "__main__":
  main()
