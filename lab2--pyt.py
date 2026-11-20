                        # UNIT -02

#1. number gussing game

import random

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the correct number!")
        break


#2(a).Write a Python program to check whether a given positive integer is a 
# Prime Number or Not a Prime Number.

num = int(input("Enter a number: "))
if num <= 1:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")


#2(b)Write a Python program to find the factorial of a positive integer using loop.
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)


#3.Write a program to generate a random OTP. Ask user to enter the no of digits(4 or 6) required for the otp. Generate the otp and print it

n = int(input("Enter number of terms: "))

a = 0
b = 1

print(a, end=" ")
print(b, end=" ")

for i in range(3, n + 1):

    c = a + b

    print(c, end=" ")

    a = b
    b = c
    
#4.Write a Python program to print the first n terms of the Fibonacci series Using Recursion.

def fibonacci(n): 
    if n == 0 or n == 1:
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2) 

n = int(input("Enter number of terms: ")) 
for i in range(n): print(fibonacci(i), end=" ") 
