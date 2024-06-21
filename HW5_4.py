def evaluate_expression(expression):
    try:
        result = eval(expression)  # Evaluates the arithmetic expression using the eval() function
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero")  # Raises a ZeroDivisionError if division by zero occurs
    except (SyntaxError, NameError):
        raise ValueError("Error: Operand error")  # Raises a ValueError for syntax or operand errors
    except Exception as e:
        raise e  # Raises other exceptions


def unsupported_characters(expression):
    valid_chars = set("0123456789+-*/()")  # Set of valid characters in the expression
    unsupported_chars = set(char for char in expression if char not in valid_chars)  # Finds unsupported characters
    return unsupported_chars  # Returns a set of unsupported characters


def valid_expression(expression):
    unsupported_chars = unsupported_characters(expression)  # Checks for unsupported characters in the expression
    return len(unsupported_chars) == 0  # Returns True if no unsupported characters found, False otherwise


def balanced_parentheses(expression):
    stack = []  # Stack to keep track of opening parentheses
    for char in expression:
        if char == "(":
            stack.append(char)  # Adds opening parentheses to the stack
        elif char == ")":
            if not stack:
                return False  # Returns False if a closing parentheses occurs without a corresponding opening parentheses
            stack.pop()  # Removes a corresponding opening parentheses from the stack
    return len(stack) == 0  # Returns True if the stack is empty (balanced parentheses), False otherwise


def evaluate_arithmetic_expression():
    while True:
        user_input = input("Enter an expression to evaluate or 'q' to quit: ")
        if user_input == "q":
            break

        unsupported_chars = unsupported_characters(user_input)  # Finds unsupported characters in the user input
        if unsupported_chars:
            print("Error: Unsupported characters in the expression:", ", ".join(unsupported_chars))
            continue  # Skips evaluation if unsupported characters are found and prompts for a new expression

        if not balanced_parentheses(user_input):
            print("Error: Unbalanced parentheses")
            continue  # Skips evaluation if parentheses are unbalanced and prompts for a new expression

        try:
            result = evaluate_expression(user_input)  # Evaluates the arithmetic expression
            print("Result:", result)
        except ZeroDivisionError as e:
            print(str(e))  # Prints division by zero error
        except ValueError as e:
            print(str(e))  # Prints operand error

evaluate_arithmetic_expression()  # Calls the main function to start the program