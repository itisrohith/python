#2.1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

M = int(input("Enter the lower bound of the interval: "))
N = int(input("Enter the upper bound of the interval: "))

print("Prime numbers within the interval:")
for num in range(M, N + 1):
    if is_prime(num):
        print(num, end=" ")
print("\nEven numbers within the interval:")
for num in range(M, N + 1):
    if num % 2 == 0:
        print(num, end=" ")


#2.2

lowernum = int(input("type any number from which you would like to find prime numbers "))
uppernum = int(input("type any number upto which you would like to find prime numbers "))

print("Prime numbers between", lowernum, "and", uppernum, "are:")

for num in range(lowernum, uppernum + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#2.3
binary1 = input("Enter the first binary number: ")
binary2 = input("Enter the second binary number: ")
binary3 = input("Enter the third binary number: ")

decimal1 = int(binary1, 2)
decimal2 = int(binary2, 2)
decimal3 = int(binary3, 2)

greatest_decimal = max(decimal1, decimal2, decimal3)
greatest_binary = bin(greatest_decimal)[2:]

print("The greatest binary number is:", greatest_binary)

#2.4
matrix = [[4, 6, 7, 8],
          [3, 7, 2, 7],
          [7, 3, 7, 5]]

transpose = []

for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

for row in transpose:
    print(row)

#2.5
import random

for i in range(10):
    num = random.randint(20,40)
    print(num)
