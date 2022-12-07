height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

w = float(weight)
h = float(height)

BMI =(w / h ** 2)
bmi_round_off = round(BMI)

print(bmi_round_off)