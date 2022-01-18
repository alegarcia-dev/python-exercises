# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Helper functions
def number_of_vowels(word):
    return len([letter for letter in word.lower() if letter in 'aeiou'])

def prime(number):
    if number <= 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(f'uppercased_fruits = {uppercased_fruits}')

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.title() for fruit in fruits]
print(f'capitalized_fruits = {capitalized_fruits}')

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if number_of_vowels(fruit) > 2]
print(f'fruits_with_more_than_two_vowels = {fruits_with_more_than_two_vowels}')

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if number_of_vowels(fruit) == 2]
print(f'fruits_with_only_two_vowels = {fruits_with_only_two_vowels}')

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_chars = [fruit for fruit in fruits if len(fruit) > 5]
print(f'fruits_with_more_than_five_chars = {fruits_with_more_than_five_chars}')
print()

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_five_chars = [fruit for fruit in fruits if len(fruit) == 5]
print(f'fruits_with_five_chars = {fruits_with_five_chars}')

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_chars = [fruit for fruit in fruits if len(fruit) < 5]
print(f'fruits_with_less_than_five_chars = {fruits_with_less_than_five_chars}')

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
number_of_chars_in_each_fruit = [len(fruit) for fruit in fruits]
print(f'number_of_chars_in_each_fruit = {number_of_chars_in_each_fruit}')

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(f'fruits_with_letter_a = {fruits_with_letter_a}')

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 == 0]
print(f'even_numbers = {even_numbers}')
print()

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]
print(f'odd_numbers = {odd_numbers}')

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
print(f'positive_numbers = {positive_numbers}')

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
print(f'negative_numbers = {negative_numbers}')

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numbers_with_two_or_more_numerals = [
                                        number
                                        for number in numbers
                                        if len(str(number).lstrip('-')) >= 2
                                    ]
print(f'numbers_with_two_or_more_numerals = {numbers_with_two_or_more_numerals}')

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number * number for number in numbers]
print(f'numbers_squared = {numbers_squared}')
print()

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers =  [
                            number
                            for number in numbers
                            if number % 2 != 0 and number < 0
                        ]
print(f'odd_negative_numbers = {odd_negative_numbers}')

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [number + 5 for number in numbers]
print(f'numbers_plus_5 = {numbers_plus_5}')

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
primes = [number for number in numbers if prime(number)]
print(f'primes = {primes}')