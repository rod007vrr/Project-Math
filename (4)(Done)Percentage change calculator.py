print("Hello, welcome to the percentage change calculator! Please input a initial value and final value and I will inform you of the percentage change")
initialValue = int(input("Initial value\n"))
finalValue = int(input("Final value\n"))
change = finalValue/initialValue
print(change*100, "percent of inital value")
if change > .1:
    print(change*100 - 100, "percent Gain")
elif change < .1:
    print((change*100 - 100)*-1, "percent loss")
elif change == 1:
    print("No change")
