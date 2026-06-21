import random

computer=random.choice([-1,0,1])

youstr=input("enter you choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"s",-1:"w",0:"g"}
you=youDict[youstr]

print(f"computer choose{reverseDict[computer]}")

if (computer==you):
    print("draw!")

if (computer==-1 and you==1):
    print("you win!")
elif (computer==-1 and you==0):
    print("you lose!")
elif (computer==1 and you==-1):
    print("you lose!")
elif (computer==0 and you==1):
    print("you lose!")
elif (computer==0 and you==-1):
    print("you win!")
elif (computer==1 and you==0):
    print("you win!")
else:
    print("something went wrong!")