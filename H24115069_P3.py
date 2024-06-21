print("Welcome to the simple calculator program!")

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Select an operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero. Please input numbers again.")
            continue
        result = num1 / num2
    else:
        print("Invalid operation. Please try again.")
        continue

    print("Result:", result)

    while True:
        choice = input("Do you want to perform another calculation? (yes or no): ")
        if choice.lower() in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter yes or no.")

    if choice.lower() == "no":
        break

print("Goodbye!")

