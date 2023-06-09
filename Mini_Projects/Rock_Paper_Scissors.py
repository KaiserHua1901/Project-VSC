import random

def Check_if_input_is_int(numb):
    while True:
        if numb.isdigit():
            if int(numb) <= 3 and int(numb) != 0:
                numb = int(numb)
                break
        else: 
            print('Please type in number & is smaller than 4 next time.')
         
        return(numb)

choice = ['rock', 'paper' , 'Scissors']
pc_guess = random.choice(choice)

print(pc_guess)

while True:
    player_choice = input("Please choice 1 for rock, 2 for paper, 3 for scissors: ")
    
    Check_if_input_is_int(player_choice)
    continue








