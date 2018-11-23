print("Hello, welcome to the equation of a linear function. Input two points on the line and I will give you the slope and y-intercept")
x1 = int(input("X coordinate of point 1\n"))
y1 = int(input("Y coordinate of point 1\n"))
x2 = int(input("X coordinate of point 2\n"))
y2 = int(input("Y coordinate of point 2\n"))
slope = (y2-y1)/(x2-x1)
yIntercept = y1-(x1*slope)

if slope == 0:
    print("y=",yIntercept)
elif yIntercept == 0:
    print("y=",slope,"x")
elif slope != 0 and yIntercept !=0 and slope > 0:
    print("The equation of your line is y = ",slope,"x +",yIntercept)
elif slope != 0 and yIntercept !=0 and slope < 0:
    print("The equation of your line is y = ",slope,"x ",yIntercept)
