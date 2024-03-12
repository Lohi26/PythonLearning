weight=int(input("Enter your weight (in kgs)="))
height=float(input("Enter your height (in cms)="))
BMI=weight/((height/100)**2)
print(f"Your BMI value = {BMI}")
if BMI<18.5:
    print("Under weight")
elif BMI>18.5 and BMI<25:
    print("Normal weight")
elif BMI>25 and BMI<30:
    print("Slightly over weight")
elif BMI>30 and BMI<35:
    print("Obese")
else:
    print("Clinically Obese")