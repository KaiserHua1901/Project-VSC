import random
from Function_project import Check_if_input_is_int

choice = [1, 2 , 3]



score = 0

while True:
    pl_choice = Check_if_input_is_int()
    pc_guess = random.choice(choice)
    print(pc_guess)
    if pl_choice == "q" or pl_choice == "Q":
        break
    else:
        if pl_choice == pc_guess:
            print('This is a draw')
        elif pl_choice == 1 and pc_guess == 2:
            print("You Lose")
            score -= 1
        elif pl_choice == 1 and pc_guess == 3:
            print('You Win')
            score += 1
        elif pl_choice == 2 and pc_guess == 1:
            print('You win')
            score += 1
        elif pl_choice == 2 and pc_guess == 3:
            print('You lose')
            score -= 1
        elif pl_choice == 3 and pc_guess == 2:
            print('You win')
            score += 1
        elif pl_choice == 3 and pc_guess == 1:
            print('You Lose')
            score -= 1

print(f'Your score is {score}')
    










