num1=float(input("enter first number:"))
operator=input("enter your operator(+,-,*,/):")
num2=float(input("enter second number:"))

if operator=="+":
    print("Result:",num1+num2)

elif operator=="-":
    print("Result:",num1-num2)

elif operator=="*":
    print("Result:",num1*num2)

elif operator=="/":
    if num2!=0:
        print("Result:",num1/num2)
    else:
        print("Division by zero is not defined")
        
else:
    print("Invalid operator")