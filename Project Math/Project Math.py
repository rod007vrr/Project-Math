import math
pi = 3.14159
print("Hello welcome to the math equation completion system")
print("What would you like to do today")
selection1 = int(input("1. Arc Length\n2. Sector Area\n3. Average Sequencer\n4. Percentage Change Calculator\n5. Prime Number Calculator\n6. Equation of a linear function\n 7. Quadriatic function solver"))
if selection1 == 1: #Arc Length
    print("Welcome to the arc length calculator!")
    circleAngle = int(input("What is the angle? "))
    circleRadius = int(input("What is the radius? "))
    print("Arc length is ", circleAngle/360 * 2 * pi * circleRadius)
    print("Other arc length is ", (360 - circleAngle)/360 * 2 * pi * circleRadius)
elif selection1 == 2: #Sector Area
    print("Hello, welcome to the Sector Area calculator! Input the angle of the selected area and the radius of your circle and I will give you both sector areas")
    circleAngle = int(input("What is the angle? "))
    circleRadius = int(input("What is the radius? "))
    print("Sector area is ", circleAngle/360 * pi * circleRadius ** 2)
    print("Other sector area is ", (360 - circleAngle)/360 * pi * circleRadius ** 2)
elif selection1 == 3: #Average Sequencer
    print("Hello, welcome to the Average Sequencer! Input two values and I will repeatedly calculate the average of theme until it reaches a whole number.")
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
elif selection1 == 4: #Percentage Change Calculator
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
elif selection1 == 5: #Prime Number Calculator
    print("Hello, welcome to the prime number calculator! Input one number and you will recieve information whether that number and all numbers below it are prime")
    howMuch = int(input("Up to what number would you like to check for primes? "))
    for n in range (2,howMuch+1):
        for x in range (2,n):
            if n % x == 0:
                print(n, "is not prime")
                break
        else:
            print(n, "is a prime number")
elif selection1 == 6:
    print("Hello, welcome to the equation finder. Input the coordinates of two points to recieve a linear function which passes through both of them")
    #WIP
