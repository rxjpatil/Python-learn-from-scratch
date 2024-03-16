print("Welcome to BMI Calculator")
weight = float(input("Enter your weight in Kg :"))
height = float(input("Enter your height in Feet :"))
meter = height * 0.3048
bmi = weight / (meter**2)
# print(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are Under Weight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have Ideal Weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you have Over Weight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you have Obese")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you have Clinacally Obese")

