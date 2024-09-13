#Taking input user name
import math


name=input("Please enter your name: ")

#Taking input favorite numbers
numbers=[]
for i in range(3):
    number=int(input(f"Enter you {i+1} favorite number:"))
    numbers.append(number)

#Greeting the user
print(f"Hello {name}, let's explore your favorite numbers.")

#Creating a list of tuples with number and whether it is even or odd
even_odd=[(num, "even" if num % 2==0 else "odd")for num in numbers]

#Checking if numbers are even or odd and displaying the information
print("Let's explore whether your numbers are even or odd:")
for num, status in even_odd:
    print(f"The number {num} is {status}")

#Calculating and print the squares of each number
print("Now let's see the squares of your favorite numbers:")
for num in numbers:
    square_tuples=(num,num**2)
    print(f"The square of {num} is {square_tuples[1]}.")

#Calculating the sum of numbers and encouraging the user
total=sum(numbers)
print(f"Wow! Well done the sum of your numbers is {total}.")

#Checking whether the sum is a prim number
if total<=1:
    print("The sum of the numbers you chose not prime number.")

elif total==2:
    print("The sum of the numbers you chose is a prime number.")

elif total%2==0:
    print("The sum of the numbers you chose not prime number.")

for i in range(3,int(math.sqrt(total))+1,2):
    if total%i==0:
        print("The sum of the numbers you chose not prime number.")

else:
    print("The sum of the numbers you chose is a prime number")