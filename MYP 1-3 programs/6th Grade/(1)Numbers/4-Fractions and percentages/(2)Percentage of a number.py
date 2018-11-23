print("Hello welcome to the percentage calculator!")
print("To find the percentage of a number press 1")
print("To find what percent what number is of another press 2")
whatDo = int(input("What do?\n"))
if whatDo == 1:
    numberStart = float(input("Number:\n"))
    percentOf = float(input("What percentage of the number do you want to recieve(Do not include percentage sign):\n"))
    print(percentOf, "percent of ", numberStart, " is ", numberStart*(percentOf/100))
if whatDo == 2:
    numberBase = float(input("Base number:\n"))
    numberChange = float(input("Changed number:\n"))
    print(numberChange, " is ", (numberChange/numberBase)*100, " percent of ", numberBase)