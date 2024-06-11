# BMI Calculator
# Don't change the code below
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# Don't change the code above

print(type(height))

# Calculate BMI
result = weight / (height * height)
print("Your BMI is:", result)

# Alternatively, you can use the ** operator for exponentiation
# bmi = weight / (height ** 2)
# print("Your BMI is:", bmi)
result_as_int = int(result)
print(result_as_int)
