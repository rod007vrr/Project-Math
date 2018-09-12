print("Hello, welcome to the average sequencer, Input two values and I will repeatedly calculate the average of theme until it reaches a whole number")
averageValue1 = int(input("Value 2\n"))
averageValue2 = int(input("Value 2\n"))
s=0
sN=0
while 1==1:
    sN+=1
    print("Sequence", sN)
    print(averageValue1)
    print(averageValue2)
    print((averageValue1+averageValue2)/2)
    s=averageValue2
    averageValue2=(averageValue1+averageValue2)/2
    averageValue1=s
    if sN>5 and averageValue2%1==0:
        break
