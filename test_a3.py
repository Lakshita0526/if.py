# -*- coding: utf-8 -*-
"""test a3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zDh7wWuR9cIfgxx1jluEQBxjKdRnb70b
"""

#  Q.1 Discount Calculation Write a program that calculates the final price of a product after applying a discount. The discount is 20% if the price is above $100, otherwise, it's 10%.
price=int(input())
if price>100:
  print(price*0.8)
else:
  print(price*0.9)

# Q.2 Grade Classification Create a program that takes a student's exam score as input and outputs whether the student passed or failed based on the following conditions:\n",
    # "\n",
    # "If the score is 90 or above: Grade A\n",
    # "\n",
    # "If the score is between 80 and 89: Grade B\n",
    # "\n",
    # "If the score is between 70 and 79: Grade C\n",
    # "\n",
    # "If the score is below 70: Fail\n",
score=int(input())
if score>=90:
  print("A grade")
elif score>80 and score<89:
  print("B grade")
elif score>70 and score<79:
  print("C grade")
elif score<70:
  print("Fail")

# "Q.3 Temperature Alert Write a program that checks the temperature of a machine. If the temperature is greater than 70°C, print a warning that the machine is overheating.\n",
temp=int(input())
if temp>70:
  print("Machine is overheating")
else:
  print("normal")

# Q.4 Driving Eligibility Write a program that checks if a person is eligible to get a driving license. \n",
    # "The person must be at least 18 years old and must pass a driving test.
x=int(input())
if x>=18:
  print("person is eligible to get a license")
else:
  print("not eligible")

# "Q.6  Odd Numbers in a Range Write a program that prints all odd numbers between 1 and 50 using a loop.
for i in range(1,51):
  if i%2!=0:
    print(i)

# "Q.7  Student Attendance Create a program that takes the number of students present each day for a month and calculates the total number of students present at the end of the month.
days_in_month = 30

total_attendance = 0

# Loop through each day to get the number of students present
for day in range(1, days_in_month + 1):
    students_present = int(input(f"Enter the number of students present on day {day}: "))
    total_attendance += students_present
print(total_attendance)

# "Q.8  Password Attempts Create a password checker where the user has 3 attempts to input the correct password. \n",
    # "After 3 wrong attempts, display an error message and terminate the program.
password=int(input())
if password==1234:
  print("correct")
else:
  print("wrong")
  print("error")

# Q.12  Shopping List Manager Write a program that allows a user to add items to a shopping list, remove items, and display the final list.
l1=[1,2,"abx","xyz",67,56]
l1.append("lakshita")
l1.remove("xyz")
print(l1)

# "Q.14   Book Collection Write a program that stores a collection of books (title, author) in tuples. Print the books sorted by title
books = [
    ("c programming", "e-balaguruswami"),
    ("xyz", "abc"),
]
sorted_books = sorted(books, key=lambda x: x[0])
print(sorted_books)

# Q.16   Product Inventory Write a program to store a product inventory where keys are product names and values are stock quantities. Add functionality to check the stock of a particular product

# "Q.17   Student Grades Create a program that stores student names as keys and their grades as values in a dictionary.\n",
    # "Allow the user to input a student's name and retrieve their grade

# Q.5  Sales Summary Given a list of daily sales figures for a week, use a loop to calculate the total sales for the week.
list=[

# "Q.9   Simple Interest Calculation Write a function that calculates the simple interest given principal, rate of interest, and time.\
def simple_interest(principal, rate, time):
  prncipal=int(input())
  rate=int(input())
  time=int(input())
  return(principal*rate*time)/100
simple_interest(100,2,3)