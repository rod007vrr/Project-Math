response = input("Hello welcome to the mixed number converter. Please enter 1 if you want to convert to a mixed number or enter 2 if you want to convert from a mixed number\n")
numerator = int(input("Numerator:\n"))
denominator = int(input("Denominator:\n"))
mixedDigit = 0
if response == "1":
    while numerator >= denominator:
        numerator -= denominator
        mixedDigit += 1
    print("Your number as a mixed number is:\n", mixedDigit, "+    (", numerator, "/", denominator,")")
if response == "2":
    mixedDigit = int(input("The mixed Digit:\n"))
    print("Your number as a improper fraction is:\n", mixedDigit*denominator + numerator, "/", denominator)