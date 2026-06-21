import random

choices=["rock","paper","scissor"]

computer=random.choice(choices)

you=input("enter your choice:").lower()
print("computer choose:",computer)

if you==computer:
    print("Draw!")

if you=="rock"and computer=="scissor":
    print("you win!")
elif you=="rock"and computer=="paper":
    print("you lose!")
if you=="paper"and computer=="scissor":
    print("you lose!")
if you=="paper"and computer=="rock":
    print("you win!")
if you=="scissor"and computer=="rock":
    print("you lose!")
if you=="scissor"and computer=="paper":
    print("you win!")
else:
    print("something went wrong!")
