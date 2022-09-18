from cmath import sqrt
import math


x = int(input("Write parameter A:"))
y = int(input("Write parameter B:"))
z = int(input("Write parameter C:"))

delta = y**2 - 4*x*z
print(delta)
pierwiastekDelta = sqrt(delta)

if delta > 0:
    print("Delta istnieje")
    print(pierwiastekDelta)
else:
    print("Delta nieistnieje")


