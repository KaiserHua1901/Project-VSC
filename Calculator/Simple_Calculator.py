symbol = input("Enter mathematic operation(+ , - , * , /): ")

if symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/':  

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    plus = round(number1 + number2, 1)
    minus = round(number1 - number2, 1)
    mutiple = round(number1 * number2, 1)
    divide = round(number1 / number2, 1)

    if symbol == "+":
        print(f'The result is {plus}')
    elif symbol == '-':
        print(f'The result is {minus}')
    elif symbol == '*':
        print(f'The result is {mutiple}')
    elif symbol == "/":
        print(f'The result is {divide}')
else:
    print("Something is wrong ")

    