# **Number exploration tool**
## Assignment:
### Python Programming Assignment: Number exploration tool
#### Instructions:
You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys exploring numbers. The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers. After gathering this information, the program should greet the user with a personalized message that includes their name. The three numbers provided by the user should be stored in a list. The program should then check if any of the numbers are even or odd, and store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd". Following this, the program should use a for loop to iterate over the list of numbers, and for each number, it should create a tuple containing the number and its square. These tuples should be printed in a creative and engaging format. Additionally, the program should calculate the sum of the three numbers and print the result, accompanied by an encouraging message. Finally, the program should determine if the sum is a prime number and notify the user with an appropriate message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their favorite numbers in a fun and interactive way, while also introducing some interesting logical checks.
```python
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
```
## Output
### Example:
Please enter your name: Rehma Khan

Enter you 1 favorite number:7

Enter you 2 favorite number:13

Enter you 3 favorite number:6

Hello Rehma Khan, let's explore your favorite numbers.

Let's explore whether your numbers are even or odd:

The number 7 is odd

The number 13 is odd

The number 6 is even

Now let's see the squares of your favorite numbers:

The square of 7 is 49.

The square of 13 is 169.

The square of 6 is 36.

Wow! Well done the sum of your numbers is 26.

The sum of the numbers you chose not prime number.