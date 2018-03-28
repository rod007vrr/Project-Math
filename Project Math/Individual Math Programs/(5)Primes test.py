print("Hello, welcome to the prime number calculator! Input one number and you will recieve information whether that number and all numbers below it are prime")
howMuch = int(input("Up to what number would you like to check for primes? "))
for n in range (2,howMuch+1):
    for x in range (2,n):
        if n % x == 0:
            print(n, "is not prime")
            break
    else:
        print(n, "is a prime number")
