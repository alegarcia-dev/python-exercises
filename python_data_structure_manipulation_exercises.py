from statistics import mean
from statistics import mode
from collections import Counter

students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# Helper variables
students_in_web_development = [student for student in students if student['course'] == 'web development']
students_in_data_science = [student for student in students if student['course'] == 'data science']

# 1. How many students are there?
#   14
print(f'#1 {len(students)}')

# 2. How many students prefer light coffee? For each type of coffee roast?
#   3
#   {'medium': 6, 'dark': 5, 'light': 3}
number_of_each_coffee_preference = Counter(student['coffee_preference'] for student in students)
print(f'#2 {number_of_each_coffee_preference["light"]}')
print(f'    {number_of_each_coffee_preference}')

# 3. How many types of each pet are there?
#   3
types_of_pets = []
for student in students:
    for pet in student['pets']:
        if pet['species'] not in types_of_pets:
            types_of_pets.append(pet['species'])

print(f'#3 {len(types_of_pets)}')

# 4. How many grades does each student have? Do they all have the same number of grades?
#   [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
number_of_grades_per_student = [len(student["grades"]) for student in students]
print(f'#4 {number_of_grades_per_student}')
print(f' Do they all have the same number of grades: {bool(len(set(number_of_grades_per_student)))}')

# 5. What is each student's grade average?
#   [78.5, 83.5, 73.25, 78.5, 81.5, 80.75, 84.5, 88.75, 88.75, 82.5, 81.5, 91, 79, 89]
grade_average_per_student = [mean(student['grades']) for student in students]
print(f'#5 {grade_average_per_student}')

# 6. How many pets does each student have?
#   [1, 0, 1, 2, 3, 0, 1, 2, 2, 1, 2, 1, 1, 1]
number_of_pets_per_student = [len(student['pets']) for student in students]
print(f'#6 {number_of_pets_per_student}')

# 7. How many students are in web development? data science?
#   7 and 7
number_students_in_web_development = len(students_in_web_development)
number_students_in_data_science = len(students_in_data_science)
print(f'#7')
print(f' Students in web development: {number_students_in_web_development}')
print(f' Students in data science: {number_students_in_data_science}')

# 8. What is the average number of pets for students in web development?
#   1.2857142857142858
average_number_pets_for_web_dev = mean(len(student['pets']) for student in students_in_web_development)
print(f'#8 {average_number_pets_for_web_dev}')

# 9. What is the average pet age for students in data science?
#   5.444
average_pet_age_for_data_science =  mean(
                                            pet['age']
                                            for student in students_in_data_science
                                            for pet in student['pets']
                                        )
print(f'#9 {average_pet_age_for_data_science}')

# 10. What is most frequent coffee preference for data science students?
coffee_preference_for_data_science = [student['coffee_preference'] for student in students_in_data_science]
print(f'#10 {mode(coffee_preference_for_data_science)}')

# 11. What is the least frequent coffee preference for web development students?
#   dark and medium are the least frequent
number_coffee_preference_for_web_dev = Counter(student['coffee_preference'] for student in students_in_web_development)
# print(f'#11 {min(number_coffee_preference_for_web_dev, key=number_coffee_preference_for_web_dev.get)}')
print(f'#11 {number_coffee_preference_for_web_dev}')

# 12. What is the average grade for students with at least 2 pets?
#   83.8, this is overall average not average of averages
students_with_at_least_two_pets =   [
                                        student
                                        for student in students
                                        if len(student['pets']) >= 2
                                    ]
average_grade_of_students_with_two_or_more_pets =   mean(
                                                            grade
                                                            for student in students_with_at_least_two_pets
                                                            for grade in student['grades']
                                                        )
print(f'#12 {average_grade_of_students_with_two_or_more_pets}')

# 13. How many students have 3 pets?
print(f'#13 {number_of_pets_per_student.count(3)}')

# 14. What is the average grade for students with 0 pets?
#   82.125, this is overall average not average of averages
students_with_zero_pets =   [
                                student
                                for student in students
                                if len(student['pets']) == 0
                            ]
average_grade_of_students_with_zero_pets =  mean(
                                                    grade
                                                    for student in students_with_zero_pets
                                                    for grade in student['grades']
                                                )
print(f'#14 {average_grade_of_students_with_zero_pets}')

# 15. What is the average grade for web development students? data science students?
#   81.178 and 84.678
average_grade_for_web_dev = mean(
                                    grade
                                    for student in students_in_web_development
                                    for grade in student['grades']
                                )
average_grade_for_data_science =    mean(
                                            grade
                                            for student in students_in_data_science
                                            for grade in student['grades']
                                        )
print(f'#15')
print(f'    average for web dev: {average_grade_for_web_dev}')
print(f'    average for data science: {average_grade_for_data_science}')

# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
#   28.8
students_with_dark_coffee_preference =  [
                                            student
                                            for student in students
                                            if student['coffee_preference'] == 'dark'
                                        ]
average_grade_range_for_dark_coffee_drinkers =  mean(
                                                        max(student['grades']) - min(student['grades'])
                                                        for student in students_with_dark_coffee_preference
                                                    )
print(f'#16 {average_grade_range_for_dark_coffee_drinkers}')

# 17. What is the average number of pets for medium coffee drinkers?
#   1.166
students_with_medium_coffee_preference =    [
                                                student
                                                for student in students
                                                if student['coffee_preference'] == 'medium'
                                            ]
average_number_pets_for_medium_coffee_drinkers =    mean(
                                                            len(student['pets'])
                                                            for student in students_with_medium_coffee_preference
                                                        )
print(f'#17 {average_number_pets_for_medium_coffee_drinkers}')

# 18. What is the most common type of pet for web development students?
#   horse
most_common_pet_for_web_dev =   mode(
                                        pet['species']
                                        for student in students_in_web_development
                                        for pet in student['pets']
                                    )
print(f'#18 {most_common_pet_for_web_dev}')

# 19. What is the average name length?
#   13.642
average_name_length = mean(len(student['student']) for student in students)
print(f'#19 {average_name_length}')

# 20. What is the highest pet age for light coffee drinkers?
#   8
students_with_light_coffee_preference = [
                                            student
                                            for student in students
                                            if student['coffee_preference'] == 'light'
                                        ]
highest_pet_age_for_light_coffee_drinkers =     max(
                                                    pet['age']
                                                    for student in students_with_light_coffee_preference
                                                    for pet in student['pets']
                                                )
print(f'#20 {highest_pet_age_for_light_coffee_drinkers}')