import random
number=0
randomNumber=0
for x in range(1):
    for x in range(10000):
        randomNumber=random.randint(-10,10)
        number = number + randomNumber
        print(number)
    number=0
    
