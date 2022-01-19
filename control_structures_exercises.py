# 1a
# Prompt the user for a day of the week, print out whether the day is Monday or not.
print('#1a')
day = input('Enter a day of the week: ')
if day.lower() == 'monday':
    print(f'{day} is Monday')
else:
    print(f'{day} is not Monday')

# 1b
# Prompt the user for a day of the week, print out whether the day is a weekday or a weekend.
print('#1b')
day = input('Enter a day of the week: ')
if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print(f'{day} is a weekday')
elif day.lower() in ['saturday', 'sunday']:
    print(f'{day} is the weekend')
else:
    print(f'{day} is not a day of the week.')

# 1c
# Create variables and make up values for
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours.
print('#1c')
number_of_hours_worked = 63
hourly_rate = 20.20

if number_of_hours_worked > 40:
    weekly_paycheck = 40 * hourly_rate + (number_of_hours_worked - 40) * hourly_rate
else:
    weekly_paycheck = number_of_hours_worked * hourly_rate

print(f'Gross income for {number_of_hours_worked} hours worked: ${weekly_paycheck:.2f}')

# 2a
# Create an integer variable i with a value of 5.
print('\n#2a')
i = 5

# Create a while loop that runs so long as i is less than or equal to 15.
# Each loop iteration, output the current value of i, then increment i by one.
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
print()
i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.
print()
i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the 
# number is less than 1,000,000. Output should equal:
print()
i = 2
while i < 1_000_000:
    print(i)
    i *= i

# Write a loop that uses print to create the output shown below (start at 100 count down by 5s to 5).
print()
i = 100
while i > 0:
    print(i)
    i -= 5

# 2b
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
print('\n#2b')
number = int(input('Enter a number: '))
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

# Create a for loop that uses print to create the output shown below. (1, 22, 333, ...)
print()
for i in range(1, 10):
    print(i * str(i))

# 2c
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to 
# continue prompting the user if they enter invalid input. (Hint: use the isdigit method on 
# strings to determine this). Use a loop and the continue statement to output all the odd 
# numbers between 1 and 50, except for the number the user entered.
print('\n#2c')

user_input = None
while True:
    user_input = input('Enter an odd number between 1 and 50: ')

    if not user_input.isdigit():
        print('That is not a number.')
        continue
    elif int(user_input) % 2 == 0:
        print('That is not an odd number.')
        continue
    elif not (1 <= int(user_input) <= 50):
        print('That is not a number between 1 and 50.') 
        continue
    break
    
print(f'Number to skip is {user_input}')
user_input = int(user_input)
for i in range(1, 51, 2):
    if i == user_input:
        print(f'Yikes! Skipping number: {i}')
        continue
    print(f'Here is an odd number: {i}')

# 2d
# Prompt the user to enter a positive number and write a loop that counts from 0 to that 
# number. (Hints: first make sure that the value the user entered is a valid number, also 
# note that the input function returns a string, so you'll need to convert this to a numeric type.)
print('\n#2d')

while True:
    user_input = input('Enter a positive number: ')

    if not user_input.lstrip('-').isdigit():
        print(f'The input {user_input} is not a number.')
    elif int(user_input) < 0:
        print(f'The input {user_input} is not a positive number.')
    else:
        break

user_input = int(user_input)
for i in range(user_input + 1):
    print(i)

# 2e
# Write a program that prompts the user for a positive integer. Next write a loop that 
# prints out the numbers from the number the user entered down to 1.
print('\n#2e')

while True:
    user_input = input('Enter a positive number: ')

    if not user_input.lstrip('-').isdigit():
        print(f'The input {user_input} is not a number.')
    elif int(user_input) < 0:
        print(f'The input {user_input} is not a positive number.')
    else:
        break

user_input = int(user_input)
for i in range(user_input, 0, -1):
    print(i)

# 3
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# - Write a program that prints the numbers from 1 to 100.
# - For multiples of three print "Fizz" instead of the number
# - For the multiples of five print "Buzz".
# - For numbers which are multiples of both three and five print "FizzBuzz".
print('\n#3')
for i in range(101):
    print(i, end = '\r')
    if i % 3 == 0:
        print('Fizz', end = '')
    if i % 5 == 0:
        print('Buzz', end = '')
    print()

# 4
# Display a table of powers.
# - Prompt the user to enter an integer.
# - Display a table of squares and cubes from 1 to the value entered.
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.
# - Bonus: Research python's format string specifiers to align the table.
print('\n#4')
continue_looping = 'y'
while continue_looping == 'y':
    user_input = input('Enter an integer: ')
    print(f'{"number":^10} | {"squared":^10} | {"cubed":^10}')
    print(f'{"":-^10} | {"":-^10} | {"":-^10}')
    
    for i in range(1, int(user_input) + 1):
        print(f'{i:<10} | {i * i:<10} | {i ** 3:<10}')

    continue_looping = input('Would you like to continue (y/n): ').strip()

# 5
# Convert given number grades into letter grades.
# - Prompt the user for a numerical grade from 0 to 100.
# - Display the corresponding letter grade.
# - Prompt the user to continue.
# - Assume that the user will enter valid integers for the grades.
# - The application should only continue if the user agrees to.
# - Grade Ranges:
#   - A : 100 - 88
#   - B : 87 - 80
#   - C : 79 - 67
#   - D : 66 - 60
#   - F : 59 - 0
# Bonus Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
print('\n#5')
continue_looping = 'y'
while continue_looping == 'y':
    user_input = int(input('Enter a numerical grade between 0 and 100: '))
    if 88 <= user_input <= 100:
        print(f'Letter grade for {user_input}: A')
    elif 80 <= user_input <= 87:
        print(f'Letter grade for {user_input}: B')
    elif 67 <= user_input <= 79:
        print(f'Letter grade for {user_input}: C')
    elif 60 <= user_input <= 66:
        print(f'Letter grade for {user_input}: D')
    elif 0 <= user_input <= 59:
        print(f'Letter grade for {user_input}: F')
    continue_looping = input('Would you like to continue (y/n): ').strip()
    
# 6
# Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. Loop through the 
# list and print out information about each book.
# - Prompt the user to enter a genre, then loop through your books list and print out the titles 
#   of all the books in that genre.
print('\n#6')
books = [
    {'title' : 'The Alchemist', 'author' : 'Paulo Coelho', 'genre' : 'Fiction'},
    {'title' : 'How Charts Lie', 'author' : 'Alberto Cairo', 'genre' : 'Non-Fiction'},
    {'title' : 'A Brief History of Time', 'author' : 'Stephen Hawking', 'genre' : 'Non-Fiction'},
    {'title' : 'The Hobbit', 'author' : 'J.R.R. Tolkien', 'genre' : 'Sci-Fi/Fantasy'},
    {'title' : 'Johnny Got His Gun', 'author' : 'Dalton Trumbo', 'genre' : 'Fiction'},
    {'title' : 'A Scanner Darkly', 'author' : 'Philip K Dick', 'genre' : 'Sci-Fi/Fantasy'}
]
length_of_column = 25
print(f'{"Title":<{length_of_column}} | {"Author":<{length_of_column}} | {"Genre":<{length_of_column}}')
print(f'{"":-<{length_of_column}} | {"":-<{length_of_column}} | {"":-<{length_of_column}}')
for book in books:
    print(f'{book["title"]:<{length_of_column}} | {book["author"]:<{length_of_column}} | {book["genre"]:<{length_of_column}}')

user_input = input('\nEnter a genre: ')
print(f'\n{"Title":<{length_of_column}} | {"Author":<{length_of_column}} | {"Genre":<{length_of_column}}')
print(f'{"":-<{length_of_column}} | {"":-<{length_of_column}} | {"":-<{length_of_column}}')
for book in [_book for _book in books if _book['genre'] == user_input]:
    print(f'{book["title"]:<{length_of_column}} | {book["author"]:<{length_of_column}} | {book["genre"]:<{length_of_column}}')