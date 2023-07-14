#TODO make a game that guess a word.

print('Welcome to guess game.')
print('The word we looking for have 5 letter.')
print("This word is say when someone do something good for you")

# What the word is
# How the player gonna find it
# Do they guess the whole words
# Or do they guess one word at the time.

#/////////////////////////////////////////////////////////////////
# THIS IS NOT WORK FIXED
# word = 'thank'

# while True:
#     guess = str(input('Enter the word or a single letter: '))
#     if guess == 'q' or 'Q':
#         break
#     if guess == 't' or 'h' or 'a' or 'n' or 'k':
#         print('There is one letter in the word')
#     elif guess == 'thank':
#         print('You guess the right word')
#         break
#     else: 
#         print('There is no letter like that in the word')
#//////////////////////////////////////////////////////////////////    

    
import random
# library that we use in order to choose
# on random words from a list of words

# name = input("What is your name? ")

# # Here the user is asked to enter the name first

# print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)


print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 12


while turns > 0:

	# counts the number of times a user fails
	failed = 0

	# all characters from the input
	# word taking one at a time.
	for char in word:

		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char, end=" ")

		else:
			print("_")

			# for every failure 1 will be
			# incremented in failure
			failed += 1

	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("You Win")

		# this print the correct word
		print("The word is: ", word)
		break

	# if user has input the wrong alphabet then
	# it will ask user to enter another alphabet
	print()
	guess = input("guess a character:")

	# every input character will be stored in guesses
	guesses += guess

	# check input with the character in word
	if guess not in word:

		turns -= 1

		# if the character doesn’t match the word
		# then “Wrong” will be given as output
		print("Wrong")

		# this will print the number of
		# turns left for the user
		print("You have", + turns, 'more guesses')

		if turns == 0:
			print("You Loose")

