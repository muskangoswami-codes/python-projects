choice=input("enter the choice (C/F):").upper()

if choice=="C":
    celcius=float(input("enter the celcius:"))
    fahrenheit= (celcius*(9/5))+32
    print("Fahrenheit:",fahrenheit)

elif choice=="F":
    fahrenheit=float(input("enter the fahrenheit:"))
    celcius=(fahrenheit-32)*(5/9)
    print("Celcius:",celcius)

else:
    print("Invalid choice")