print("Welcome Here :) ")
playing = input('Will you play Quiz game ? ')
if playing.lower() != 'yes':
    quit()
print("okay ! lets play game..")
score = 0

answer = input('What is full form of GF ')
if answer.lower() == 'girl friend':
    print('Correct !!')
    score += 1
else:
    print('Wrong!!')
 
answer = input('What is full form of BF ')
if answer.lower() == 'boy friend':
    print('Correct !!')
    score += 1
else:
    print('Wrong!!')
     
answer = input('What is full form of GG ')
if answer.lower() == 'good job':
    print('Correct !!')
    score += 1
else:
    print('Wrong!!')
print("You got  " + str(score) + "Correct Answers" )
print("You got  " + str((score / 3) * 100) + "%." )