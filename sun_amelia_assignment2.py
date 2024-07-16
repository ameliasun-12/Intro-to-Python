#1. Write a for loop that prints the numbers from 1 to 10, one per line.
for i in range (1,11):
    print(i)
print('\n')

#2. Write a for loop that iterates over a list of names and prints “Hello, name” for each name in the list.
name_list = ["Jeremy", "Jane", "John", "Julia"]

for name in name_list:
    print(f"Hello, {name}.")
print('\n')

#3. Write a for loop that calculates the sum of all the elements in a list of numbers and prints the result.
num_list = [1,2,5,7,8,12]
sum = 0

for num in num_list:
    sum += num

print(sum)
print('\n')

#4. Write a for loop that reverses a string and prints the reversed string.

my_string = "hello"
def reverse(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text
    return rev_text

print(reverse(my_string))
print('\n')

#5. Write a for loop that counts how many times each letter appears in a string and prints the letter and its frequency.

letter_count = {}
for char in my_string:
     if char in letter_count.keys():
        letter_count[char] += 1
     else:
        letter_count[char] = 1

for char, count in letter_count.items():
    print(f'{char}:{count}')
print('\n')

#6. Write a for loop that iterates over a dictionary of students and their grades and prints the name and grade of each student who passed the course.

stu_grades = {
    "Grace": 76,
    "Dylan": 92,
    "Jennifer": 40,
    "Hunter": 84,
    "Jordan": 52,
}

for stu, grade in stu_grades.items():
    if grade >= 60:
        print(f"{stu} passed with a grade of {grade}")
print('\n')

#7. Write a for loop that prints the multiplication table for a given number n.

n = 8
table_range = 10

for i in range(1, table_range+1):
    print(f"{n} x {i} = {n*i}")
print('\n')

#8. Write a while loop that prints the numbers from 1 to 10, one per line.
i = 0
while i < 11:
    print (i)
    i += 1
print('\n')

#9. Write a while loop that asks the user to enter a name and prints "Hello, [name]" until the user enters "quit".
on = True 
while on:
    name = input("Enter a name or type 'quit' to stop:")
    if name.lower() == 'quit':
        on = False
    else:
        print(f"Hello, {name}!")

print('\n')

#10. Write a program that asks the user to enter a number and prints whether it is even or odd using an if else statement.

num_on = True 
while num_on:
    user_input = input("Enter a number to check if it is odd or even. Type 'quit' to stop:")
    if user_input.lower() == "quit":
        num_on = False
        break
    
    num = int(user_input)
    if num % 2 > 0:
        print(f"{num} is odd")
    else:
        if num == 0:
            print(f"{num} is neither")
        elif num % 2 == 0:
            print(f"{num} is even")

print('\n')

#11. Write a program that creates a list of 10 random numbers between 1 and 100 and prints the smallest and the largest number in the list using a loop and an if else statement.

import random
random_num = [random.randint(1,100) for _ in range(10)]
smallest = random_num[0]
largest = random_num[0]

for num in random_num:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num

print("The smallest number is:", smallest)
print("The largest number is:", largest)
print('\n')

#12. Write a program that creates a dictionary with the keys being the names of some fruits and the values being their prices. Then, ask the user to enter a fruit name and print the price of that fruit using an if else statement. If the fruit name is not in the dictionary, print "Sorry, we don't have that fruit."

fruit_inventory = {
    "apples": 1.25,
    "bananas": 1.00,
    "oranges": 1.75,
    "pears": 1.10,
    "grapes": 0.75,    
}
fruit_name = input("Enter a fruit name").lower()

if fruit_name in fruit_inventory:
    print(f"The price of {fruit_name} is ${fruit_inventory[fruit_name]:.2f}")
else:
    print:("Sorry, we don't have that fruit.")