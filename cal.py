def calculator():
    print("Welcome to the Simple Calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:     
        print("Invalid input! Please enter numeric values.")
        return

    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nError: Cannot divide by zero!")
    else:
        print("\nInvalid operation selected!")

# Run the calculator
calculator()
