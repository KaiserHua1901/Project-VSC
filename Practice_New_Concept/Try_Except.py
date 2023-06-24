# while True:
#     try:
#         x = int(input("Enter a number greater than 0: "))
#         if x <= 0:
#             raise ValueError("Number must be greater than 0")
#             # this will make the code show the value error then loop back to the first thing in loop
#         break
#     except ValueError as e:
#         print(e)
#         # This will show the error and show that it not working.
# print("You entered:", x)



while True:
    try:
        x = int(input("Please Enter a number: ")) 
        if str(x).isdigit() or x > 0:
            print(f"{x} is a digit")
        if x <= 0:
            raise ValueError('It needed to be larger than 0')
        break
    except TypeError as x:
        print(f"{x} is not a digit, Please enter a digit")
    #this will check if the x is a digit
    # THIS IS NOT WORKING
print(type(x))
# def check_digit(x):
#     while True:
#         if str(x).isdigit() and int(x) > 0:
#             break
#         else:
#             print(f'You need to enter a number and is larger than 0')
#             x = input('Please Enter the number here again: ')
            
#     return int(x)

# number = int(input("Please Enter a number: "))
# #you put this as a int but in check it to make sure it an int before use it, a failsafe.
# check_digit(number)
# print(type(number))

