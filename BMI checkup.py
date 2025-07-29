weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in cm:"))
BMI= weight/(height/100)**2
print("Your BMI is",BMI)

if BMI < 18.5:
    print("You're underweight")
elif BMI < 24.5:
    print("You're healthy")
elif BMI < 30.5:
    print("You're overweight")
else:
    print("You're obese")