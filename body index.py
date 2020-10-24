weight=float(input("Enter your weight in kg:: "))
height=float(input("Enter your height in meters:: "))
bmi=weight/(height**height)

print("BMI is ",round(bmi,2),"Which are")

if(bmi<=18.5):
    print("Underweight")
elif(bmi>18.5 and bmi<=24.9):
    print("Normal weight")
elif(bmi>24.9 and bmi<=29.9):
    print("Overweight")
elif(bmi>=30):
    print("Obesity")

