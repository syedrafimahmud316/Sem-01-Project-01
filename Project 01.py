'''
Write a program that reads a three-digit integer n (assume it is positive and three-digit).

Your program must:

Extract its three digits using // and %.

Determine whether all three digits are different (print "All different" or "Not all different").

Using the math module, print the factorial of the largest digit.

Print the absolute difference between the largest and smallest digits.

If the number formed by the digits is even, print "Even", otherwise "Odd".
'''




import math

num = int(input("Enter your three-digit number: "))

a = (num // 100) % 10
b = (num // 10) % 10
c = num % 10

if (a == b == c):
    print(f"All the same.")
elif (a == b) or (b == c) or (c == a):
    print(f"Some of the digits are same.")
else: 
    print(f"All different.")

max_ = max(a,b,c)
min_ = min(a,b,c)

factorial = math.factorial(max_)
print(f"The factorial of the maximum digit {max_} is n! = {factorial}.")


absoulute_difference = abs(abs(max_) - abs(min_))
print(f"The absolute difference between the largest and smallest digits is {absoulute_difference}.")



if (num % 2 == 0):
    print("Even.")
else:
    print("Odd.") 