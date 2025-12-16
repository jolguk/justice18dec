def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")

def get_operation():
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        if choice in ("1", "2", "3", "4", "5"):
            return choice
        print("Invalid choice, please select 1, 2, 3, 4, or 5.")

def main():
    print("Simple Calculator")

    while True:
        choice = get_operation()

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(num1, num2)
                op_symbol = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                op_symbol = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                op_symbol = "*"
            elif choice == "4":
                result = divide(num1, num2)
                op_symbol = "/"

            print(f"Result: {num1} {op_symbol} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

        print("-" * 30)

if __name__ == "__main__":
    main()