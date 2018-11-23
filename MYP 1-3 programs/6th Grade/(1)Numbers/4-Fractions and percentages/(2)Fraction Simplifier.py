print("Welcome to the Fraction Simplifier. Please input the Numerator and Denominator of your fraction to recieve your answer")
numerator = int(input("Numerator:\n"))
denominator = int(input("Denominator:\n"))
numOriginal = numerator
denOriginal = denominator
for n in range(denominator, 2,-1):
    if numerator%n == 0 and denominator%n == 0:
        numerator = numerator/n
        denominator = denominator/n
print(numOriginal, "/", denOriginal, " simplified is, ", numerator,"/",denominator)