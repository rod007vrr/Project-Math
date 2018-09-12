print("Hello, welcome to the different base converter. To use this just input what number you would like to convert to base 10 and the base to convert from")
baseToConvertFrom = int(input("Base to convert from:\n"))
numberToConvert = int(input("Number to convert to base 10\n"))
print(
    (int(str(numberToConvert)[len(str(numberToConvert))-1]) * baseToConvertFrom**0) + (int(str(numberToConvert)[len(str(numberToConvert))-2]) * baseToConvertFrom**1)
)