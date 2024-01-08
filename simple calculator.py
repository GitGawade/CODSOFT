def calculator():
    print("Welcome to the simple calculator!")

    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    print("Choose an operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input("Your choice (1-4): "))

    # Perform the calculation and display the result
    if operation == 1:
        result = num1 + num2
        print(f"The result is: {result}")
    elif operation == 2:
        result = num1 - num2
        print(f"The result is: {result}")
    elif operation == 3:
        result = num1 * num2
        print(f"The result is: {result}")
    elif operation == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please choose a number between 1 and 4.")

# Run the calculator
calculator()
