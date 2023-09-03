from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    continues = True
    num1 = float(input("\nEnter the first number: "))
    for symbol in operations:
            print(symbol)
    while continues:
        operation = input("\nPick an operation: ") 
        num2 = float(input(("\nEnter the second number: ")))
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"\nType 'y' if you want to continue calculating with {answer}, type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else: 
            continues = False
            calculator()


calculator()
        