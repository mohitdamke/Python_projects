import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a  greater number")
else:
    print("Type a number..")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number...")
        continue
     
    if user_guess == random_number:
        print("Good job ;) ")
    
    elif user_guess > random_number:
        print("Choise a smaller number..")
    
    else:
        print("You are below the number!.")