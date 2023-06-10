
def Check_if_input_is_int():
    while True:
        numb = input("Please choice 1 for rock, 2 for paper, 3 for scissors, Q to quit: ")
        if numb == 'Q' or numb == "q":
            break
        
        if numb.isdigit():
            numb = int(numb)
            if int(numb) <= 3 and int(numb) != 0:
                numb = int(numb)
                break
            else: 
                print('Please type in number smaller than 4 next time.')
        else: 
            print('please type in a number')
        
    return(numb)