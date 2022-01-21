from string import ascii_uppercase, ascii_lowercase, digits

# 1
# Define a function named is_two. It should accept one input and return True if the 
# passed input is either the number or the string 2, False otherwise.

# Walkthrough
# 1. When we pass the string value '2' (i.e. is_two('2')) the function will perform two checks: 
#    - if n == '2' (which in this case is True since '2' == '2')
#    - if n == 2 (which is False since '2' != 2)
#    The function uses the or operator so only one condition needs to be true. Since the first condition is true
#    the function will return True.
# 2. When we pass the int value 2 (i.e. is_two(2)) the function will perform two checks: 
#    - if n == '2' (which is False since 2 != '2')
#    - if n == 2 (which in this case is True since 2 == 2)
#    The function uses the or operator so only one condition needs to be true. Since the second condition is true
#    the function will return True.
# 3. When we pass the string value '22' (i.e. is_two('22')) the function will perform two checks: 
#    - if n == '2' (which is False since '22' != '2')
#    - if n == 2 (which is False since '22' != 2)
#    The function uses the or operator so only one condition needs to be true. Since both conditions are false the
#    function will return False.

def is_two(n) -> bool:
    '''
        Parameter(s):
            n: str or int

        Return value:
            bool

        Description:
            Return True if the argument is the string value '2' or int value 2,
            otherwise return False.
    '''
    return n == '2' or int(n) == 2

print(f'# 1')
print(f'Is "2" two? {is_two("2")}')
print(f'Is 2 two? {is_two(2)}')
print(f'Is 222 two? {is_two(222)}')
print(f'Is "222" two? {is_two("222")}')
print(f'Is "-2" two? {is_two("-2")}')
print(f'Is -2 two? {is_two(-2)}')
print(f'Is True two? {is_two(True)}')
print(f'Is False two? {is_two(False)}')

# 2
# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# Walkthrough
# 1. When we pass the string value 'e' (i.e. is_vowel('e')) the function will perform two checks:
#    - the function checks the boolean value of the string, which will be False if it is an empty string
#      and True otherwise.
#    - the string is converted to all lowercase and the function checks if the string is in the string 'aeiou',
#      that is it checks if the string equals either 'a', 'e', 'i', 'o', or 'u'.
#    The function uses the and operator so if the string is a vowel and not empty it will return True. In this
#    case 'e' is a vowel and not an empty string so the function returns True.
# 2. When we pass the string value 'r' (i.e. is_vowel('r')) the function will perform two checks:
#    - the function checks the boolean value of the string, which will be False if it is an empty string
#      and True otherwise.
#    - the string is converted to all lowercase and the function checks if the string is in the string 'aeiou',
#      that is it checks if the string equals either 'a', 'e', 'i', 'o', or 'u'.
#    The function uses the and operator so if the string is a vowel and not empty it will return True. In this
#    case 'r' is not a vowel and not an empty string so the function returns False since (False and True) is False.

def is_vowel(character: str) -> bool:
    '''
        Parameter(s):
            character: str (a single character is expected)

        Return value:
            bool

        Description:
            Return True if the argument is a vowel, otherwise return False.
    '''
    # First verify the string is not empty, then check if it is a vowel.
    return bool(character) and character.lower() in 'aeiou'

print(f'\n# 2')
print(f'Is "a" a vowel? {is_vowel("a")}')
print(f'Is "e" a vowel? {is_vowel("e")}')
print(f'Is "i" a vowel? {is_vowel("i")}')
print(f'Is "o" a vowel? {is_vowel("o")}')
print(f'Is "u" a vowel? {is_vowel("u")}')
print(f'Is "t" a vowel? {is_vowel("t")}')
print(f'Is "r" a vowel? {is_vowel("r")}')
print(f'Is "w" a vowel? {is_vowel("w")}')
print(f'Is "m" a vowel? {is_vowel("m")}')
print(f'Is "x" a vowel? {is_vowel("x")}')
print(f'Is "O" a vowel? {is_vowel("O")}')
print(f'Is "A" a vowel? {is_vowel("A")}')
print(f'Is "" a vowel? {is_vowel("")}')

# 3
# Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

# Walkthrough
# 1. When we pass the string value 'e' (i.e. is_vowel('e')) the function will perform two checks:
#    - the function checks the boolean value of the string, which will be False if it is an empty string
#      and True otherwise.
#    - the string is then passed to the is_vowel function and the function checks if the string is not a vowel.
#    The function uses the and operator so if the string is not a vowel and not empty it will return True. In this
#    case 'e' is a vowel and not an empty string so the function returns False since not is_vowel('e') will evaluate
#    to False.
# 2. When we pass the string value 'r' (i.e. is_vowel('r')) the function will perform two checks:
#    - the function checks the boolean value of the string, which will be False if it is an empty string
#      and True otherwise.
#    - the string is then passed to the is_vowel function and the function checks if the string is not a vowel.
#    The function uses the and operator so if the string is not a vowel and not empty it will return True. In this
#    case 'r' is not a vowel and not an empty string so the function returns True.

def is_consonant(character: str) -> bool:
    '''
        Parameter(s):
            character: str (a single character is expected)

        Return value:
            bool
        
        Description:
            Return True if the argument is a consonant, otherwise return False.
    '''
    # First verify the string not empty, then check if it is not a vowel
    return bool(character) and not is_vowel(character)

print(f'\n# 3')
print(f'Is "a" a consonant? {is_consonant("a")}')
print(f'Is "e" a consonant? {is_consonant("e")}')
print(f'Is "i" a consonant? {is_consonant("i")}')
print(f'Is "o" a consonant? {is_consonant("o")}')
print(f'Is "u" a consonant? {is_consonant("u")}')
print(f'Is "t" a consonant? {is_consonant("t")}')
print(f'Is "r" a consonant? {is_consonant("r")}')
print(f'Is "w" a consonant? {is_consonant("w")}')
print(f'Is "m" a consonant? {is_consonant("m")}')
print(f'Is "x" a consonant? {is_consonant("x")}')
print(f'Is "O" a consonant? {is_consonant("O")}')
print(f'Is "A" a consonant? {is_consonant("A")}')
print(f'Is "Y" a consonant? {is_consonant("Y")}')
print(f'Is "H" a consonant? {is_consonant("H")}')
print(f'Is "" a consonant? {is_consonant("")}')

# 4
# Define a function that accepts a string that is a word. The function should capitalize the first 
# letter of the word if the word starts with a consonant.

# Walkthrough
# 1. When we pass the string value 'word' (i.e. capitalize_if_consonant('word')) the function will return the 
#    word capitalized (using the capitalize function) if the first letter is a consonant. It is determined whether
#    or not first letter is a consonant by utilizing the is_consonant function and passing as argument word[0]
#    which in this case will pass the letter 'w'. is_consonant will return True since 'w' is a consonant and the
#    argument capitalized will be returned.
# 2. When we pass the string value 'apple' (i.e. capitalize_if_consonant('apple')) the function will return the 
#    word capitalized (using the capitalize function) if the first letter is a consonant. It is determined whether
#    or not first letter is a consonant by utilizing the is_consonant function and passing as argument word[0]
#    which in this case will pass the letter 'a'. is_consonant will return False since 'a' is a vowel and the
#    function will use the else clause to return the argument unchanged.

def capitalize_if_consonant(word: str) -> str:
    '''
        Parameter(s):
            word: str

        Return value:
            str

        Description:
            Return the string with the first letter converted to uppercase if the first letter
            is a consonant, otherwise return the input unchanged.
    '''
    return word.capitalize() if is_consonant(word[0]) else word

print(f'\n# 4')
print(f'Capitalize "word"? {capitalize_if_consonant("word")}')
print(f'Capitalize "apple"? {capitalize_if_consonant("apple")}')
print(f'Capitalize "hungry"? {capitalize_if_consonant("hungry")}')
print(f'Capitalize "underwear"? {capitalize_if_consonant("underwear")}')
print(f'Capitalize "buns"? {capitalize_if_consonant("buns")}')

# 5
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and 
# the bill total, and return the amount to tip.

# Walkthrough
# 1. When we pass 0.15 (as our percentage) and 20.00 (as our total) to the function it will multiply these two 
#    numbers (which will result in 3). This result is then rounded to two decimal places (using the round function)
#    which gives us the result 3.00.
# 2. When we pass 0.20 (as our percentage) and 76.53 (as our total) to the function it will multiply these two 
#    numbers (which will result in 15.306). This result is then rounded to two decimal places (using the round 
#    function) which gives us the result 15.31.

def calculate_tip(percentage: float, total: float) -> float:
    '''
        Parameter(s):
            percentage: float (expects a number between 0 and 1)
            total: float

        Return value:
            float

        Description:
            Determine the amount of the tip by multiplying percentage and total and round the result to two
            decimal places.
    '''
    return round(percentage * total, 2)

print(f'\n# 5')
print(f'15% tip for $20 bill: ${calculate_tip(0.15, 20.00):.2f}')
print(f'10% tip for $50 bill: ${calculate_tip(0.1, 50.00):.2f}')
print(f'20% tip for $76.53 bill: ${calculate_tip(0.2, 76.53):.2f}')
print(f'0% tip for $5.05 bill: ${calculate_tip(0, 5.05):.2f}')
print(f'80% tip for $253.02 bill: ${calculate_tip(0.8, 253.02):.2f}')

# 6
# Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

# Walkthrough
# 1. When we pass 20.00 (as out total) and 15 (as our discount) the function will perform several calculations. 
#    The discount will be converted to a decimal value by dividing discount by 100 (in this case 0.15), this result
#    is multiplied by the total in order to calculate the total discount (in this case 3), then that result is 
#    subtracted from the total (in this case 17) in order to get the discounted total. The result is then rounded
#    to two decimal places using the round function.

def apply_discount(total: float, discount: float) -> float:
    '''
        Parameter(s):
            total: float
            dicount: float (as percentage between 0 and 100)

        Return value:
            float

        Description:
            Determine the amount of discount to apply and subtract that amount from the total. Round the result
            to two decimal places.
    '''
    return round(total - (total * (discount / 100)), 2)

print(f'\n# 6')
print(f'$20 bill with 15% off: ${apply_discount(20.00, 15):.2f}')
print(f'$52.43 bill with 5% off: ${apply_discount(52.43, 5):.2f}')
print(f'$134.02 bill with 20% off: ${apply_discount(134.02, 20):.2f}')
print(f'$4 bill with 50% off: ${apply_discount(4.00, 50):.2f}')
print(f'$40 bill with 0% off: ${apply_discount(40.00, 0):.2f}')

# 7
# Define a function named handle_commas. It should accept a string that is a number that contains commas 
# in it as input, and return a number as output.

# Walkthrough
# 1. When we pass '1,000,000' as an argument (i.e. handle_commas('1,000,000')) the function will create a new string
#    with all the commas (',') replace with empty strings (''). In this case the result will be '1000000'. This
#    result will be converted to an integer (using the int function) and that result will be returned.

def handle_commas(number_with_commas: str) -> int:
    '''
        Parameter(s):
            number_with_commas: str

        Return value:
            int

        Description:
            Replace all commas in the argument with empty strings and convert the result to an integer.
    '''
    return int(number_with_commas.replace(',', ''))

print(f'\n# 7')
print(f'1,000,000 without commas: {handle_commas("1,000,000")}')
print(f'4,809 without commas: {handle_commas("4,809")}')
print(f'7,401,722,300,875 without commas: {handle_commas("7,401,722,300,875")}')
print(f'10,000,000,000,000,000 without commas: {handle_commas("10,000,000,000,000,000")}')
print(f'1,00,22,33 without commas: {handle_commas("1,00,22,33")}')

# 8
# Define a function named get_letter_grade. It should accept a number and return the letter grade 
# associated with that number (A-F).

# Walkthrough

# 1. When we pass 43 as our argument (i.e. get_letter_grade(43)) this input will be checked against each range
#    of values through a series of if, elif and else blocks. The first condition that evaluates to True will 
#    determine which letter grade should be returned. In this case the condition (43 in range(60)) will evaluate
#    to True since the range function will provide the range 0 - 59 and 43 is in that range. So as a result 'F' will
#    be returned.
# 2. When we pass 89 as our argument (i.e. get_letter_grade(89)) this input will be checked against each range
#    of values through a series of if, elif and else blocks. The first condition that evaluates to True will 
#    determine which letter grade should be returned. In this case the condition (89 in range(80, 90)) will evaluate
#    to True since the range function will provide the range 80 - 89 and 89 is in that range. So as a result 'B' will
#    be returned.

def get_letter_grade(number_grade: int) -> str:
    '''
        Parameter(s):
            number_grade: int

        Return value:
            str

        Description:
            Determine the letter grade for the provided numeric grade using the following conversion table:
                90 - 100 is an A
                80 - 89 is a B
                70 - 79 is a C
                60 - 69 is a D
                0 - 59 is a F
            Otherwise return 'Invalid Input'.
    '''
    if number_grade in range(90, 101):
        return 'A'
    elif number_grade in range(80, 90):
        return 'B'
    elif number_grade in range(70, 80):
        return 'C'
    elif number_grade in range(60, 70):
        return 'D'
    elif number_grade in range(60):
        return 'F'
    else:
        return 'Invalid Input'

print(f'\n# 8')
print(f'Letter grade for 43: {get_letter_grade(43)}')
print(f'Letter grade for 60: {get_letter_grade(60)}')
print(f'Letter grade for 76: {get_letter_grade(76)}')
print(f'Letter grade for 89: {get_letter_grade(89)}')
print(f'Letter grade for 92: {get_letter_grade(92)}')
print(f'Letter grade for 1000: {get_letter_grade(1000)}')

# 9
# Define a function named remove_vowels that accepts a string and returns a string with all the 
# vowels removed.

# Walkthrough
# 1. When we pass "hungry" to the function (i.e. remove_vowels("hungry")) the function will evaluate the generator
#    comprehension which will produce each character in string_with_vowels if the character is a consonant (for which 
#    we use the is_consonant function). So 'h' when passed to is_consonant will evaluate to True so 'h' will be 
#    produced by the comprehension. Then 'u' when passed to is_consonant will evaluate to False so 'u' will not be
#    produced by the comprehension. We continue until checking each character in string_with_vowels. After we have
#    iterated over each character the results will be joined together (using the join function) with empty strings
#    between each character (meaning all the consonants are joined together into a single word). The result of this
#    is returned.

def remove_vowels(string_with_vowels: str) -> str:
    '''
        Parameter(s):
            string_with_vowels: str

        Return value:
            str

        Description:
            Return a string that is the argument with all vowels removed.
    '''
    return ''.join(character for character in string_with_vowels if is_consonant(character))

print(f'\n# 9')
print(f'"hungry" without vowels: {remove_vowels("hungry")}')
print(f'"banana" without vowels: {remove_vowels("banana")}')
print(f'"anaconda" without vowels: {remove_vowels("anaconda")}')
print(f'"tch" without vowels: {remove_vowels("tch")}')
print(f'"" without vowels: {remove_vowels("")}')
print(f'"oi" without vowels: {remove_vowels("oi")}')

# 10
# Define a function named normalize_name. It should accept a string and return a valid python identifier, 
# that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#   - Name will become name
#   - First Name will become first_name
#   - % Completed will become completed

# Walkthrough
# 1. When we pass "First Name" as an argument (i.e. normalize_name("First Name")) the function will first pass the
#    argument to the remove_invalid_characters function with the argument converted to all lowercase. As the name 
#    implies the purpose of the remove_invalid_characters function is to remove any characters that are not valid
#    for use in Python identifiers. It does this by first going through each character in the string and only 
#    accepting those characters which are either an alphabetic letter, a number,an underscore or a space. In this
#    case all characters in "First Name" are valid so the string is unchanged. Then any leading numbers are removed
#    (meaning any numbers at the beginning of the string), this is done by iterating over the string until a non
#    numerical character is found and reassigning the string everything after the first character for each number.
#    In this case there are no leading numbers so the string is unchanged and the result returned. Next back in the
#    normalize_name function any leading or trailing whitespace is removed from the string using the strip function.
#    Finally, all remaining spaces are replaced with underscores, using the replace function, and the result is 
#    returned. The result is "first_name"
# 2. When we pass "% Completed" as an argument (i.e. normalize_name("% Completed")) the function will first pass the
#    argument to the remove_invalid_characters function with the argument converted to all lowercase. As the name 
#    implies the purpose of the remove_invalid_characters function is to remove any characters that are not valid
#    for use in Python identifiers. It does this by first going through each character in the string and only 
#    accepting those characters which are either an alphabetic letter, a number,an underscore or a space. In this
#    case all characters in "% Completed" except the '%' are valid so the remaining string will be " completed". Then 
#    any leading numbers are removed (meaning any numbers at the beginning of the string), this is done by iterating 
#    over the string until a non numerical character is found and reassigning the string everything after the first 
#    character for each number. In this case there are no leading numbers so the string is unchanged and the result 
#    returned. Next back in the normalize_name function any leading or trailing whitespace is removed from the string
#    using the strip function. In this case there is a leading space so the remaining string is "completed".
#    Finally, all remaining spaces are replaced with underscores, using the replace function, and the result is 
#    returned. In this case there are no remaining spaces and the result is "completed".

def remove_invalid_characters(invalid_identifier: str) -> str:
    '''
        Parameter(s):
            invalid_identifier: str

        Return value:
            str

        Description:
            Remove all characters which are not valid characters for Python identifiers from the string, including
            leading numbers.
    '''
    # Only accept characters which are letters a-z, numbers 0-9,an underscore or a space
    removed_chars = ''.join(
        ch
        for ch in invalid_identifier
        if ch in ascii_lowercase or ch in digits or ch in '_ '
    )

    # Remove all leading numbers
    removed_leading_digits = removed_chars
    while removed_leading_digits[0] in digits:
        removed_leading_digits = removed_leading_digits[1 : ]
    
    return removed_leading_digits

def normalize_name(invalid_identifier: str) -> str:
    '''
        Parameter(s):
            invalid_identifier: str

        Return value:
            str

        Description:
            Turn the argument into a valid Python identifier by removing all invalid characters, leading numbers,
            any leading or trailing whitespace, and replace inner whitespace with underscores.
    '''
    # Use remove_invalid_characters function to remove all invalid characters and leading numbers
    removed_invalid_characters = remove_invalid_characters(invalid_identifier.lower())

    # Remove leading and trailing whitespace
    removed_wrapping_spaces = removed_invalid_characters.strip()

    # Replace inner spaces with underscores
    return removed_wrapping_spaces.replace(' ', '_')

print(f'\n# 10')
print(f'"Name" normalized: {normalize_name("Name")}')
print(f'"First Name" normalized: {normalize_name("First Name")}')
print(f'"% Completed" normalized: {normalize_name("% Completed")}')
print(f'"already_valid_id" normalized: {normalize_name("already_valid_id")}')
print(f'"       lots of whitespace          " normalized: {normalize_name("       lots of whitespace          ")}')
print(f'"ALL CAPS" normalized: {normalize_name("ALL CAPS")}')
print(f'"too         much" normalized: {normalize_name("too         much")}')
print(f'"12345leading_numbers " normalized: {normalize_name("12345leading_numbers ")}')
print(f'"invalid_c**h#a%r,,,.s" normalized: {normalize_name("invalid_c**h#a%r,,,.s")}')
print(f'"trailing numbers1234" normalized: {normalize_name("trailing numbers1234")}')

# 11
# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative 
# sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# Walkthrough
# 1. When we pass [1, 1, 1] as an argument (i.e. cumulative_sum([1, 1, 1])) the function utilizes a list
#    comprehension to produce a list that is the cumulative sum of the argument. The for loop in the list
#    comprehension iterates from 0 up to but not including the length of the list (which in this case is 3). Each
#    element produced by the comprehension will be the sum of the list from index 0 up to the value
#    of index in the current iteration of the for loop. One is added to index to ensure that the value of index is
#    included. In the first iteration of the for loop we get the sum of list_of_nums[0 : 0 + 1] which will simply be
#    1. Next we get the sum of list_of_nums[0 : 1 + 1] which will be 1 + 1 = 2. Finally we get the sum of 
#    list_of_nums[0 : 2 + 1] which will be 1 + 1 + 1 = 3 giving us the result of [1, 2, 3].

def cumulative_sum(list_of_nums: list) -> list:
    '''
        Parameter(s):
            list_of_nums: list[int]

        Return value:
            list[int]

        Description:
            Return a list that is a cumulative sum of the elements from the list passed
            as an argument.
    '''
    return [sum(list_of_nums[0 : index + 1]) for index in range(len(list_of_nums))]

print(f'\n# 11')
print(f'Cumulative sum of [1, 1, 1]: {cumulative_sum([1, 1 ,1])}')
print(f'Cumulative sum of [1, 2, 3, 4]: {cumulative_sum([1, 2, 3, 4])}')
print(f'Cumulative sum of [10, 23, 45, 1, 5, 22]: {cumulative_sum([10, 23, 45, 1, 5, 22])}')
print(f'Cumulative sum of [1, -1, 1, -1, 1, -1]: {cumulative_sum([1, -1, 1, -1, 1, -1])}')
print(f'Cumulative sum of [0, 0, 0, 0, 0, 0, 0]: {cumulative_sum([0, 0, 0, 0, 0, 0, 0])}')
print(f'Cumulative sum of [-1, -2, -3, -4]: {cumulative_sum([-1, -2, -3, -4])}')
print(f'Cumulative sum of [1, 0, 1, 0, 1]: {cumulative_sum([1, 0, 1, 0, 1])}')

# BONUS
# 1
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string
# that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
def format_hour_to_24(hour: str, minute: str) -> tuple:
    '''
        Parameter(s):
            hour: str
            minute: str

        Return value:
            tuple (returned as (hour, minute))

        Description:
            A helper function for twelveto24() which properly formats the hour string
            for representation in 24 hour time.
    '''
    # Add 12 to the hour if the time is pm. If the hour is 12 change it to 0 so
    # the result will be correct.
    if hour == '12':
        hour = '0'
    if 'pm' in minute:
        hour = str(int(hour) + 12)

    # Pad any single digit hours with a leading 0
    hour = f'{hour:0>2}'
    return hour, minute

def twelveto24(twelve_hour_time: str) -> str:
    '''
        Parameter(s):
            twelve_hour_time: str

        Return value:
            str

        Description:
            Convert the argument from 12 hour time to 24 hour time.
    '''
    # After formatting the hour (see format_hour_to_24 function) rejoin the
    # hour and minute into one string and strip the am/pm.
    modified_time = ':'.join(format_hour_to_24(*twelve_hour_time.split(':')))
    return modified_time.rstrip('am').rstrip('pm')

def twentyfourto12(twentyfour_hour_time: str) -> str:
    '''
        Parameter(s):
            twentyfour_hour_time: str

        Return value:
            str

        Description:
            Convert the argument from 24 hour time to 12 hour time.
    '''
    # Subtract 12 from the hour if it is greater than 12, change it
    # to 12 if it is 0 and add am/pm as appropriate. Converting 
    # the hour to an int helps with the calculation and removes
    # any leading 0.
    hour, minute = twentyfour_hour_time.split(':')
    hour = int(hour)
    if hour >= 12:
        minute += 'pm'
        hour -= 12
    else:
        minute += 'am'
    if hour == 0:
        hour = 12
    return ':'.join([str(hour), minute])

print(f'\nBONUS # 1')
print(f'10:45am converted to 24 hour time: {twelveto24("10:45am")}')
print(f'4:30pm converted to 24 hour time: {twelveto24("4:30pm")}')
print(f'11:45pm converted to 24 hour time: {twelveto24("11:45pm")}')
print(f'12:30am converted to 24 hour time: {twelveto24("12:30am")}')
print(f'12:43pm converted to 24 hour time: {twelveto24("12:43pm")}')
print(f'5:00am converted to 24 hour time: {twelveto24("5:00am")}')
print(f'10:45 converted to 12 hour time: {twentyfourto12("10:45")}')
print(f'16:30 converted to 12 hour time: {twentyfourto12("16:30")}')
print(f'23:45 converted to 12 hour time: {twentyfourto12("23:45")}')
print(f'00:30 converted to 12 hour time: {twentyfourto12("00:30")}')
print(f'12:43 converted to 12 hour time: {twentyfourto12("12:43")}')
print(f'05:00 converted to 12 hour time: {twentyfourto12("05:00")}')

# 2
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number 
# of the column.
# - col_index('A') returns 1
# - col_index('B') returns 2
# - col_index('AA') returns 27

def col_index(column: str) -> int:
    '''
        Parameter(s):
            column: str

        Return value:
            int

        Description:
            Determine the 1-based index of the spreadsheet column. Input should be an alphabetic string.
            0 is returned if the input is invalid.
    '''
    # Verify that the input is valid
    if type(column) != str or not column.isalpha():
        return 0

    # Starting from the last character in the string determine the numeric value of the character
    # (A = 1, Z = 26) and multiply by 26 raised to the power of the character's position in the string
    # where the last character is in position 0, the second to last is in position 1, etc. Sum the 
    # values of each character to get the column index.
    index = 0
    for idx, value in enumerate(column[:: -1].upper()):
        index += (ascii_uppercase.index(value) + 1) * (26 ** idx)
    return index

print(f'\nBONUS # 2')
print(f'Column index for "A": {col_index("A")}')
print(f'Column index for "B": {col_index("B")}')
print(f'Column index for "AA": {col_index("AA")}')
print(f'Column index for "Z": {col_index("Z")}')
print(f'Column index for "R": {col_index("R")}')
print(f'Column index for "AD": {col_index("AD")}')
print(f'Column index for "AAA": {col_index("AAA")}')
print(f'Column index for "": {col_index("")}')
print(f'Column index for "": {col_index(0)}')
print(f'Column index for "": {col_index(None)}')
print(f'Column index for "": {col_index(True)}')