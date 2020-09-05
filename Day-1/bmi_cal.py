#Adult Body Mass Index Calculator

import math

height = float(input("Enter your height in meters => "))
weight = float(input("Enter your weight in kilogram => "))

BMI = weight / math.pow(height, 2)

print("Your BMI is = ", BMI)