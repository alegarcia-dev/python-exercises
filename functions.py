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