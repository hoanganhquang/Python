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


def calculate():
    num1 = float(input("What's the first number? "))
    num2 = float(input("What's the second number? "))

    _recursion = True
    while _recursion:
        operations_symbol = input("Pick an operation: ")
        cal = operations[operations_symbol]
        result = round(cal(num1, num2), 2)
        print(f"{num1} {operations_symbol} {num2} = {result}")

        _continue = input("Y or N: ")
        if _continue == "y":
            num1 = result
            num2 = int(input("What's the next number? "))
            _recursion = True
        elif _continue == "n":
            _recursion = False
            calculate()
        else:
            return False


calculate()
