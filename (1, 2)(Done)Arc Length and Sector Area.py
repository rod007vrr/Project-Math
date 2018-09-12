pi = 3.14159
print("Welcome to the arc length and sector area calculator!")
circleAngle = int(input("What is the angle\n"))
circleRadius = int(input("What is the radius\n"))
print("Circle area is", circleRadius ** 2 * pi)
print("Circumference is", 2 * pi * circleRadius)
print("Arc length is ", circleAngle/360 * 2 * pi * circleRadius)
print("Sector area is ", circleAngle/360 * pi * circleRadius ** 2)
print("Other arc length is ", (360 - circleAngle)/360 * 2 * pi * circleRadius)
print("Other sector area is ", (360 - circleAngle)/360 * pi * circleRadius ** 2)


