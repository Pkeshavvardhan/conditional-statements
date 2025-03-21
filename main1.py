height=float(input("enter the height in cm"))
weight=float(input("enter the weight in kg"))

BMI= weight/(height/100)**2

print("the BMI is ", BMI)

if BMI<=18.4:
    print("you are underweight")
elif BMI<=24.9:
    print("you are normal weight")
elif BMI<=29.9:
    print("you are overweight")
else:
    print("you are obese")
    