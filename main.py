def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in ('+', '-', '*', '/'):
            break
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()