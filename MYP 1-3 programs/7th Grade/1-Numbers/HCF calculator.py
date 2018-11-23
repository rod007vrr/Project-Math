print("Welcome to the HCF calculator. Please input two numbers to recieve their HCF.")
n1 = int(input("First number:\n"))
n2 = int(input("Second number:\n"))
nOG1 = n1
nOG2 = n2
nL = n1
if n1>n2:
    nL=n1
elif n1<n2:
    nl=n2
factorsN1 = []
factorsN2 = []
HCF=1
for n in range(2,n1):
    while n1%n == 0:
        n1 = n1/n
        factorsN1.append(n)
for n in range(2,n2):
    while n2%n == 0:
        n2 = n2/n
        factorsN2.append(n)
for n in range(2,nL):
    while n in factorsN1 and n in factorsN2:
        HCF *=n
        factorsN1.remove(n)
        factorsN2.remove(n)
print("The highest common factor of ", nOG1, " and ",nOG2, " is ", HCF)
