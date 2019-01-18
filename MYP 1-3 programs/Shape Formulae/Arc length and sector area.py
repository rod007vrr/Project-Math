import math
math.pi = 3.14159
print("Welcome to the arc length and sector area calculator!")
circleAngle = float(input("What is the angle\n"))
circleRadius = float(input("What is the radius\n"))
print("Circle area is", circleRadius ** 2 * math.pi)
print("Circumference is", 2 * math.pi * circleRadius)
print("Arc length is ", circleAngle/360 * 2 * math.pi * circleRadius)
print("Sector area is ", circleAngle/360 * math.pi * circleRadius ** 2)
print("Other arc length is ", (360 - circleAngle)/360 * 2 * math.pi * circleRadius)
print("Other sector area is ", (360 - circleAngle)/360 * math.pi * circleRadius ** 2)
