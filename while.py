# Basic While Loops Questions
# 1. Print 1 to 10 using while loop. 

i = 0
while i < 10:
    i += 1
    print(i)

# 2. print even number from 2 to 20 

i = 0 
while i < 20:
    i += 2
    print(i)

# #print the sum of numbers from 1 to 100 
num = 1 
total = 0 
while num <= 100:
    total += num
    num += 1
# print("the sum of numbers from 1 to 100 is ", total)

num = 1 
total = 0 
while num <= 500:
    total += num
    num += 1
print(total)

num = 1 
total = 0 
while num <= 200:
    total += num
    num += 1
print(total)

num = 1 
total = 0 
while num <= 300:
    total += num
    num += 1
print(total)

num = 1 
total = 0 
while num <= 400:
    total += num
    num += 1
print(total)

# Take a number input and print its multiplication table (up to 10).
num = int(input("enter the number; "))
i = 1
while i <= 10:
    print(num * i)
    i += 1 

num = int(input(" enter the number: "))
i = 1 
while i <= 100:
    print(num * i)
    i += 1
 
# Reverse a number using while loop.

i = 50
while i >= 1:
    i -= 1
    print(i)

# Count the number of digits in an input number.
# # Take input from user
# num = int(input("Enter a number: "))

# # Initialize a counter
# count = 0

# # If the number is 0, it has 1 digit
# if num == 0:
#     count = 1
# else:
#     # Make number positive (to handle negative input)
#     num = abs(num)

#     # Count digits using while loop
#     while num > 0:
#         num //= 10  # Remove the last digit
#         count += 1  # Increase count

# # Print the result
# print("Number of digits is:", count)