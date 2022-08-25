#Formulas: Distance, Quadratic, and Slope

#Distance formula Calculation

import math

while True:
  x_coordinates = input("Enter the x coordinates (include a space): ")
  y_coordinates = input("Enter the y coordinates (include a space): ")
  x_coordinates = [int(x) for x in x_coordinates.split(" ")]
  y_coordinates = [int(x) for x in y_coordinates.split(" ")]
  
  if (len(x_coordinates) > 2) or (len(y_coordinates) > 2):
    print("Please enter 2 x and y coordinates.")
    continue
  else:
    break

total_x = (x_coordinates[-1] - x_coordinates[0]) ** 2
total_y = (y_coordinates[-1] - y_coordinates[0]) ** 2
total = total_x + total_y
total = math.sqrt(total)
print(total)

#Quadratic Formula Calculation

import math

a = int(input("Enter the 'a' value: "))
b = int(input("Enter the 'b' value: "))
c = int(input("Enter the 'c' value: "))

neg = False
  
while True:
    if b < 0 and c < 0 or a < 0 and b < 0 and c < 0:
        neg = True
        if neg == True:
            print(f"y = {a}x^2{b}x{c}x")
            break
    if b < 0:
        neg = True
        if neg == True:
            print(f"y = {a}x^2{b}x+{c}x") 
            break
    if c < 0:
        neg = True
        if neg == True:
            print(f"y = {a}x^2+{b}x{c}x")
            break
    else:
        print(f"Your quadratic equation: y = {a}x^2+{b}x+{c}x")
        break

if b < 0:
  x_add = (abs(b) + math.sqrt((b ** 2) - (4*a*c))) / (2*a) 
  x_subtract = (abs(b) - math.sqrt((b ** 2) - (4*a*c))) / (2*a) 
else:
  x_add = (-abs(b) + math.sqrt((b ** 2) - (4*a*c))) / (2*a) 
  x_subtract = (-abs(b) - math.sqrt((b ** 2) - (4*a*c))) / (2*a)
  
print(f"Roots: x = {x_add}, and x = {x_subtract}")

#Slope Formula Calculation

import math

while True:
  fpair = input("Enter the first pair of x & y coordinates (include a space): ")
  spair = input("Enter the second pair of x & y coordinates (include a space): ")
  fpair = [int(x) for x in fpair.split(" ")]
  spair = [int(x) for x in spair.split(" ")]
  
  if (len(fpair) > 2) or (len(spair) > 2):
    print("Please enter eaxctly 2 pairs of x and y coordinates, with 2 values each.")
    continue
  else:
    break
  
difference_1 = int(spair[-1]) - int(fpair[-1])
difference_2 = int(spair[0]) - int(fpair[0])
total = difference_1 / difference_2

isfloat = False

if type(total) == float:
  isfloat = True
  if isfloat == True:
    print(f"{difference_1} / {difference_2}")
  else:
    print(total)
