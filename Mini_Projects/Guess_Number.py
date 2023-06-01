import random

#TODO 
# - Have a maximum number that user choice to guess 
# - Make a random number that NOT above number user choice and NOT below 0
# - Have user input that choice a random number, and keep repeat until user right.
# - Score system of how many guess user need for finishing it

number = (input('Please choice a maximum number: '))

#Check to see if number is digit and > 0
if number.isdigit() and int(number) > 0: 
    number = int(number)

else: 
    print('Please type in number & is larger than 0 next time.')
    quit()
#Check to see if number is digit and > 0

#Random number with the maximum is number varible.
random_number = random.randint(0, number)


print(random_number)
score = 0

while True:
    guess = input('type a guess: ')
    score += 1
    if guess.isdigit() and int(guess) >= 0: 
        guess = int(guess)

    else: 
        print('Please type in number & is larger than -1 next time.')
        continue
    
    if guess == random_number:
        print('You Got a right answer')
        break
    elif guess < random_number:
        print('Your guess is smaller than the answer')
    elif guess > random_number:
        print("Your guess is larger than the answer")
        
print(f'Your took {score} time to guess it right!')