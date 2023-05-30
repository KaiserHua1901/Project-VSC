import random

number = (input('Please choice a maximum number: '))

if number.isdigit() and int(number) > 0: 
    number = int(number)

else: 
    print('Please type in number & is larger than 0 next time.')
    quit()

random_number = random.randint(0, number)

guess = input('type a guess: ')
print(guess)
print(random_number)