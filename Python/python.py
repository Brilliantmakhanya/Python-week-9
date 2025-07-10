# Numeric Data
num = 3
print(type(num))

num2 = 3.14
print(type(num2))

# Variables
my_variable = 10
total_count = 0
user = 'john'

# Operators
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%)
# Exponent (**)

x = 10
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(5 % 2)
print(x ** y)

# Assignment Operators
x = 10
x *= 2
print(x)

# Control statements
num = 0

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("This number is negative")

# Control statements pt2
numA = int(input("Enter the first number: "))
numB = int(input("Enter the second number: "))

if numA > numB:
    print(numA, "is greater than", numB)
elif numB > numA:
    print(numB, "is greater than", numA)
else:
    print("Both numbers are equal.")

# For Loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

numbers = [1, 2, 3, 5, 7]
for number in numbers:
    print(number)

# While Loops
count = 1
while count <= 5:
    print(count)
    count += 1

# Loops pt2 (control systems) - for loop
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        continue
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        pass
    print(fruit)

# Loops pt2 (control systems) - while loop
count = 0
while count <= 5:
    print(count)
    if count == 3:
        break
    count += 1





    


