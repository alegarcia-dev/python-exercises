# 1
# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know 
# yet if they're going to like it). If price for a movie per day is 3 dollars, 
# how much will you have to pay?

price_of_movie_per_day = 3
days_rented_per_title = {'The Little Mermaid' : 3,
                         'Brother Bear' : 5,
                         'Hercules' : 1}

total_cost = sum(price_of_movie_per_day * days for days in days_rented_per_title.values())
print(f'# 1 total_cost = {total_cost}')

# 2
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
# and Facebook 350. How much will you receive in payment for this week? You worked 10 
# hours for Facebook, 6 hours for Google and 4 hours for Amazon.

companies = {'Google', 'Amazon', 'Facebook'}

hours_worked = {'Google' : 6,
                'Amazon' : 4,
                'Facebook' : 10}

hourly_rate = {'Google' : 400,
               'Amazon' : 380,
               'Facebook' : 350}

total_payment = sum(hours_worked[company] * hourly_rate[company] for company in companies)
print(f'# 2 total_payment = {total_payment}')

# 3
# A student can be enrolled to a class only if the class is not full and the class 
# schedule does not conflict with her current schedule.

def can_enroll_in_course(course, student_schedule, course_catalog):
    if is_course_full(course_catalog[course]):
        return False

    for _course in student_schedule:
        if conflicts_with_schedule(course_catalog[_course], course_catalog[course]):
            return False

    return True

def is_course_full(course_info):
    return course_info['maximum_capacity'] == course_info['students_enrolled']

def conflicts_with_schedule(course1, course2):
    return (course2['start_time'] < course1['start_time'] < course2['end_time'] or
           course2['start_time'] < course1['end_time'] < course2['end_time'])

classes = {'Programming with Python' : {'maximum_capacity' : 30,
                                        'students_enrolled' : 27,
                                        'start_time' : 8,
                                        'end_time' : 10},
           'Data Science'            : {'maximum_capacity' : 30,
                                        'students_enrolled' : 24,
                                        'start_time' : 7,
                                        'end_time' : 9},
           'Advanced Data Analysis'  : {'maximum_capacity' : 30,
                                        'students_enrolled' : 30,
                                        'start_time' : 11,
                                        'end_time' : 13},
           'Deeply Learning'         : {'maximum_capacity' : 30,
                                        'students_enrolled' : 17,
                                        'start_time' : 13,
                                        'end_time' : 15}}

my_schedule = {'Programming with Python'}
print('# 3')
print(f'    Can enroll in Data Science: {can_enroll_in_course("Data Science", my_schedule, classes)}')
print(f'    Can enroll in Advanced Data Analysis: {can_enroll_in_course("Advanced Data Analysis", my_schedule, classes)}')
print(f'    Can enroll in Deeply Learning: {can_enroll_in_course("Deeply Learning", my_schedule, classes)}')

# 4
# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

def is_offer_valid(is_premium, offer_expired, items_in_cart):
    return (is_premium and not offer_expired) or (items_in_cart > 2 and not offer_expired)

product_offers = {'Free Milk' : {'is_expired' : False},
                  'Half Off Cereal' : {'is_expired' : True},
                  'Free Toaster Oven' : {'is_expired' : False}}

print('# 4')
print(f'    Is product offer valid (Non-Premium member, Free Milk offer, 3 items in cart): {is_offer_valid(False, product_offers["Free Milk"]["is_expired"], 3)}')
print(f'    Is product offer valid (Premium member, Half Off Cereal offer, 1 item in cart): {is_offer_valid(True, product_offers["Half Off Cereal"]["is_expired"], 1)}')
print(f'    Is product offer valid (Premium member, Free Toaster Oven offer, 4 items in cart): {is_offer_valid(True, product_offers["Free Toaster Oven"]["is_expired"], 4)}')
print(f'    Is product offer valid (Non-Premium member, Free Milk offer, 2 items in cart): {is_offer_valid(False, product_offers["Free Milk"]["is_expired"], 2)}')

# 5
username = 'codeup'
password = 'notastrongpassword'
print('# 5')

# the password must be at least 5 characters
is_password_long_enough = len(password) >= 5
print(f'    is_password_long_enough: {is_password_long_enough}')

# the username must be no more than 20 characters
is_username_short_enough = len(username) <= 20
print(f'    is_username_short_enough: {is_username_short_enough}')

# the password must not be the same as the username
is_password_same_as_username = username == password
print(f'    is_password_same_as_username: {is_password_same_as_username}')

# bonus neither the username or password can start or end with whitespace
stripped_username = username.strip()
stripped_password = password.strip()
does_username_or_password_have_whitespace = (username != stripped_username) or (password != stripped_password)
print(f'    does_username_or_password_have_whitespace: {does_username_or_password_have_whitespace}')