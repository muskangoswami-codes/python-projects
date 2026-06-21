import random

print("="*50)
print("WELCOME TO THE NUMBER GUESSING GAME!!")
print("="*50)

secret_number = random.randint(1,100)

while True:
    guess=int(input("guess a number between (1,100):"))

    if guess< secret_number:
        print("Low!")
    elif guess> secret_number:
        print("High!")
    else:
        print("Congratulation! you guessed the number")
        break

print("THANK YOU! FOR PLAYING THE GAME.")