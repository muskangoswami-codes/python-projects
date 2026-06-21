weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in m:"))

bmi=weight/(height**2)

print("BMI=",round(bmi,2))

if bmi<18.5:
    print("Underweight")
elif 18.5<bmi<25:
    print("Normal weight")
elif 25<bmi<30:
    print("Overweight")
else:
    print("obese")