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
        ranswer = round(answer, 2)
        print(f"{num1} {operation} {num2} = {answer}")
        new = input(f"\nType 'y' if you want to continue calculating with {answer}, type 'n' to start a new calculation or type 'e' to exit: ")
        if  new == 'y':
            num1 = answer
        elif new == 'n': 
            continues = False
            calculator()
        else:
            break

calculator()
        