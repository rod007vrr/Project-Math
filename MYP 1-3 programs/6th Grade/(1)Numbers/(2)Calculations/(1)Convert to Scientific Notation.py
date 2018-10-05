print("Hello, welcome to the scientific notation converter. To use this converter simply input the number you would like to convert to scientific notation")
numberToConvert = float(input("Number to convert to scientific notation:\n"))
powerOf10 = 0
baseNumber = numberToConvert
if numberToConvert >=1:
    while baseNumber / 10 > 1:
        baseNumber = baseNumber/10
        powerOf10 += 1
elif numberToConvert < 1:
    while baseNumber < 1:
        baseNumber = baseNumber*10
        powerOf10 -=1
print(numberToConvert, "in scientific notation is\n", baseNumber, "E", powerOf10)