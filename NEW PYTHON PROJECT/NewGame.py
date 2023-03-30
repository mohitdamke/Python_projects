name = input("Type your name : " )
print("Welcome", name , "to the game ! ")
answer = input("You are in a jungle , there a two ways to get out of jungle , left side and right side ,choise one of them ? ").lower()
if answer == "left":
    answer = input("There is a lion, you want to go there or not")
    if answer == "go":
        print("yes you can go")
    elif answer == "no":
        print("no you cant go")
    else:
        print("Type a valid answer")

elif answer == "right":
    answer = input("There is a beer, you want to go there or not")
    
    if answer == "go":
        print("yes you can go")
    elif answer == "no":
        print("no you cant go")
    else:
        print("Type a valid answer")
else:
    print("Type a valid answer")
print("Thankyou for playing" , name)