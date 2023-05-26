from time import sleep

print('Welcome to the Quiz game')
game = input('Do you want to play(y/n): ')

if game.lower() == 'n':
    quit()
elif game.lower() == 'y':
    print("Let Play The Game")
    sleep(0.5)

print('The first question is:')
sleep(0.5)
print("'What is CPU stand for?'")
sleep(0.5)
print('1. Central Processing Unit')    
sleep(0.5)
print('2. Centel Prompt Unit')
sleep(0.5)
print('3. Center Control')
sleep(0.5)
print('4. All above is wrong')
sleep(0.5)
answer = input('Please choice 1 to 4: ')
score = 0
if answer == "1":
    print('You are correct!')
    score += 1
elif answer == '2':
    print('You are incorrect!')
elif answer == '3':
    print('You are incorrect!')
elif answer == '4':
    print('You are incorrect!')

sleep(1)
print('Next question')
sleep(0.5)
print('What is PSU stand for?')
sleep(0.5)
print('1. Psychic supply')
sleep(0.5)
print('2. Power Supply')
sleep(0.5)
print('3. Proccesing Supply Unit')
sleep(0.5)
print('4. All above is wrong')
sleep(0.5)


answer = input('Please choice 1 to 4: ')

if answer == "1":
    print('You are incorrect!')
    score += 1
elif answer == '2':
    print('You are correct!')
    score += 1
elif answer == '3':
    print('You are incorrect!')
elif answer == '4':
    print('You are incorrect!')

sleep(1)
print('This is the end!')
print(f' You got {score * 100} point')