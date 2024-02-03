num1 = int(input("Enter number 1: "))#Store first Number.
num2 = int(input("Enter number 2: "))#Store second Number.
exp = input("Enter expression (+, -, *, /): ")#Expression

operator = {'+': 'Addition', '-': 'Subtraction', '*': 'Multiplication', '/': 'Division'}

if exp in operator:
    result = eval(f"{num1} {exp} {num2}") # eval function used to evaluate the expression
    print(f"{operator[exp]} of {num1} and {num2} is: {result}")#result
else:
    print("Please enter a valid expression (+, -, *, /)")
