print("Welcome to the vertex form converter, please input the coefficients and constacts for quadriatics")
a = int(input("The A coefficient:\n"))
b = int(input("The B coefficient:\n"))
c = int(input("The C coefficient:\n"))
h = (-1*b)/(2*a)
k = (a*(h**2))+(b*h)+c
print("{}x^2 + {}x + {} in vertex form is".format(a,b,c))
print(a,"(x-", h, ")+",k)
