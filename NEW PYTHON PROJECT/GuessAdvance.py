import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Write a number betw 1 to {x}: "))
        if guess < random_number:
            print("To Low ")
        elif guess > random_number:
            print("To High")
    print("YAAAA YOU WIN THE GAME.....")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} to high(H), too low (L), or correct(C) ?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yaaaa computer guess your number,{guess},correctly .....')


computer_guess(10)