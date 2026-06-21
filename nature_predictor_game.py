import random

print("*"*50)
print("WELCOME TO NATURE PREDICTOR GAME!!")
print("*"*50)

traits=["sweet","funny","loyal","creative",
        "imaginative","arrogant","chaotic","kind",
        "determined","hardworking","angrybird",
        "agressive","selfish","helpful","dishonest",
        "lazy","attention seeker","trustworthy",
        "caring","curious"]

while True:
    name=input("enter your name:")

    random.seed(name.lower())
    result=random.choice(traits)

    print("Hello",name+"!")
    print("\nYour predicted nature is:")
    print(result)

    print("\nNte:this game is for fun and entertainment!")
    choice=input("\nDo you want to try another name(yes/no):")
    
    if choice!="yes":
        print("\nThank you for playing the game!") 