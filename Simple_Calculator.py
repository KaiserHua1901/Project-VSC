symbol = input("Enter mathematic operation(+ , - , * , /): ")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

divide = round(number1 / number2,)

if symbol == "+":
    print(f'The result is {number1 + number2}')
elif symbol == '-':
    print(f'The result is {number1 - number2}')
elif symbol == '*':
    print(f'The result is {number1 * number2}')
elif symbol == "/":
    print(f'The result is {divide}')
else:
    print("There is no operation with that symbol")

    