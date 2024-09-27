def convert(feet_inches):
    feet, inches = feet_inches.split(" ")
    return f"{feet_inches} = {round(float(feet) * 0.3048 + float(inches) * 0.0254, 2)} meters"


feet_inches = input("Enter feet and inches: ")
print(convert(feet_inches))