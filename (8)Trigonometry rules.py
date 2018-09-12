import math
print("Hello, welcome to the Trignometry rule system! Follow directions to recieve your answer and input all values in degrees.")
selectionTrigRules = int(input("Type 1 to choose Sine rule to find missing side.\n Type 2 to choose sine rule to find missing angle.\nType 3 to choose cosine rule for missing side.\nType 4 to choose cosine rule for missing angle.\nType 5 to find the height of an object from the distance between two angles.\n Type 6 to find the area of a triangle from 2 sides and an angle inbetween"))
if selectionTrigRules == 1:
    angleA = input("Angle A")
    angleB = input("Angle B")
    sideA = input("Side A")
    sideB = (math.sin(angleB)*sideA)/math.sin(sideA)
    print("The missing side is",sideB)
if selectionTrigRules == 2:
    angleA = input("Angle A")
    sideA = input("Side A")
    sideB = input("Side B")
    sideB
if selectionTrigRules==5:
    angleA = float(input("The larger angle"))
    angleB = float(input("The smaller angle"))
    distanceBetween = float(input("Distance between those two angles"))