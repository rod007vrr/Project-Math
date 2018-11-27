from fractions import Fraction
print("Hello, welcome to the combined probability calculator. Please input the number of possible outcomes, and  the number of desired outcomes for both tests and you will recive the combined probability.")
pOCA = int(input("The total number of outcomes for test A:\n"))
dOCA = int(input("The amount of desired outcomes out of the possible outcomes for test A:\n"))
pOCB = int(input("The total number of outcomes for test B:\n"))
dOCB = int(input("The amount of desired outcomes out of the possible outcomes for test B:\n"))
denominator = pOCA*pOCB
#Function definition
def fractionSimplify(numerator, denominator):
    for n in range(denominator, 2,-1):
        if numerator%n == 0 and denominator%n == 0:
            numerator /=n
            denominator /=n
    return Fraction(numerator/denominator)
#Desired Both
numDesBoth = dOCA*dOCB
print("The chances of desired outcomes coming from both tests are", fractionSimplify(numDesBoth,denominator))
#Desired None
numAntiDesBoth = (pOCA-dOCA)*(pOCB-dOCB)
print("The chances of desired outcomes coming from no tests are", fractionSimplify(numAntiDesBoth,denominator))
#Desired A
numDesA = (dOCA)*(pOCB-dOCB)
print("The chances of desired outcomes coming from only test A are", fractionSimplify(numDesA,denominator))
#Desired B
numDesB = (dOCB)*(pOCA-dOCA)
print("The chances of desired outcomes coming from only test B are", fractionSimplify(numDesB,denominator))
