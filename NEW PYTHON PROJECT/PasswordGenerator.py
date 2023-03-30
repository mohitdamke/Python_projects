import numbers
import random
print("Welcome to password generator")
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().'
number = input('Amount of password to generates: ')
number = int(number)
length = input('Your password length: ')
length = int(length)
print('\nhere are your passwords: ')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)