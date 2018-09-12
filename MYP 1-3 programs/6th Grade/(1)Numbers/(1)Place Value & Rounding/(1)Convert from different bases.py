print("Hello, welcome to the different base converter. To use this just input what number you would like to convert to base 10 and the base to convert from")
inputBase = int(input("Base to convert from\n"))
numberToConvert = int(input("Number to convert\n"))
finalVal = 0
for n in range(0,len(str(numberToConvert))):
    finalVal += (numberToConvert%(10**(n+1))-numberToConvert%(10**n))/(10**n) * (inputBase**n)
print(numberToConvert, " in base ", inputBase, " is ", finalVal, "in base 10.")
