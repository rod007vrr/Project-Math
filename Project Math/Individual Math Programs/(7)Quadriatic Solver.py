import cmath
print("Hello, welcome to the quadriatic solver! Please input the a, b , and c values of your quadriatic function and you will recieve both roots")
a = int(input("The a of your quadriatic function\n"))
b = int(input("The b of your quadriatic function\n"))
c = int(input("The c of your quadriatic function\n"))
discriminant = (b**2) - 4*(a)*(c)
solution1 = ((-b)+cmath.sqrt(discriminant))/2*(a)
solution2 = ((-b)-cmath.sqrt(discriminant))/2*(a)
print("Your solutions are",solution1,"and",solution2)