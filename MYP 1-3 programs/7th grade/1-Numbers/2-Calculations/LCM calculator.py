print("Welcome to the LCM calculator. Please input two numbers to recieve their LCM.")
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
LCM=n1
for n in range(2,n1+1):
    while n1%n == 0:
        n1 = n1/n
        factorsN1.append(n)
print(factorsN1)
for n in range(2,n2+1):
    while n2%n == 0:
        n2 = n2/n
        factorsN2.append(n)
print(factorsN2)
for n in range(2,nL):
    while n in factorsN1 and n in factorsN2:
        factorsN1.remove(n)
        factorsN2.remove(n)
for n in range(len(factorsN2)):
    LCM *= factorsN2[n]
print("The lowest common multiplier of ", nOG1, " and ",nOG2, " is ", LCM)
