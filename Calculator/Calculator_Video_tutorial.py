from Operation_func import *
while True:
    print('What operation you want to do')
    print('Press 1 to do addtion')
    print('Press 2 to do substraction')
    print('Press 3 to do Multiply')
    print('Press 4 to do Divide')
    print('Press Q to stop the operation')
    
    choice =input('Enter your choice: ')
    if choice == 'Q' or choice == 'q':
        break
    
    
    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))


    if choice == '1':
        addition(num1, num2)

    elif choice == '2':
        substract(num1, num2)
        
    elif choice == '3':
        multiply(num1, num2)

    elif choice == '4':
        divide(num1, num2)
    else:
        print('There is no operation with that choice')
    print('\n')