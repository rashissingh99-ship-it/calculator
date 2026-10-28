def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def read_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculator():
    print("=" * 30)
    print("   SIMPLE CALCULATOR")
    print("=" * 30)

    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1-5.")
            continue

        num1 = read_number("Enter first number: ")
        num2 = read_number("Enter second number: ")

        if choice == "1":
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")


if __name__ == "__main__":
    calculator()
