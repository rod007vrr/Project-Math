print("Hello, welcome to the linear function finder. Input the coordinates of two points to recieve a linear function which passes through both of them")
x1 = float(input("X value for coordinate 1\n"))
y1 = float(input("Y value for coordinate 1\n"))
x2 = float(input("X value for coordinate 2\n"))
y2 = float(input("Y value for coordinate 2\n"))
slope = ((y2-y1)/(x2-x1))
intercept = (y2-(slope * x2))
print("Equation is",slope ,"x +",intercept)
