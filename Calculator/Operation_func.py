def addition(num1, num2):
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
    
def substract(num1, num2):
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
    
def multiply(num1, num2):
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')

def divide(num1, num2):
    if num2 == 0:
        print(f"Can't divide by 0")
    else:
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
    
    