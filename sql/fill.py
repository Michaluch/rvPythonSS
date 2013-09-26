import string
import random
import time

import MySQLdb as mysql

####################################
#########      Generating users
####################################
f_name = 'Mike', 'Tom', 'Jim', 'John', 'Chris', 'Rob', 'Robert', 'Dick', 'Barak', 'Samuel'
l_name = 'Bush', 'Obama', 'Daniels', 'Connor', 'Burton', 'Bennington', 'Henderson', 'Amerson', 'Chainey', 'Bravo'
email = 'gmail.com', 'yahoo.com', 'mail.ru', 'hotmail.com'
role_id = '1', '2'
reg_date = time.strftime('%Y-%m-%d %H:%M:%S'),
status = '1', '0'

description_1p = 'Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Aenean lacinia bibendum nulla sed consectetur. Nullam id dolor id nibh ultricies vehicula ut id elit. Aenean lacinia bibendum nulla sed consectetur.'
description_2p = """Donec sed odio dui. Nullam id dolor id nibh ultricies vehicula ut id elit. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Vestibulum id ligula porta felis euismod semper. Nulla vitae elit libero, a pharetra augue.
Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras mattis consectetur purus sit amet fermentum. Integer posuere erat a ante venenatis dapibus posuere velit aliquet."""
description_4p = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mattis consectetur purus sit amet fermentum. Maecenas faucibus mollis interdum. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
Etiam porta sem malesuada magna mollis euismod. Etiam porta sem malesuada magna mollis euismod. Nulla vitae elit libero, a pharetra augue. Nullam id dolor id nibh ultricies vehicula ut id elit. Cras justo odio, dapibus ac facilisis in, egestas eget quam.
Cras justo odio, dapibus ac facilisis in, egestas eget quam. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla vitae elit libero, a pharetra augue. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Cras justo odio, dapibus ac facilisis in, egestas eget quam.
Donec sed odio dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id elit non mi porta gravida at eget metus. Cras mattis consectetur purus sit amet fermentum. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus."""

sentence = 'Aenean lacinia bibendum nulla sed consectetur. Donec ullamcorper nulla non metus auctor fringilla. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Cras mattis consectetur purus sit amet fermentum. Vestibulum id ligula porta felis euismod semper.'
sentence = sentence.lower().replace('.', '').split()
def get_words(count):
    result = ''
    for i in range(count):
        result += random.choice(sentence)+' '
    return result

def generate_user(**lists):
    result = {}
    for key, value in lists.items():
        if len(value) >= 2:
            result[key] = random.choice(value)
        else:
            result[key] = value[0]

    def generate_password():
        letters = string.ascii_lowercase
        result = ""
        for i in range(8):
            if random.random() >= 0.5:
                result += letters[random.randrange(len(letters) - 1)]
            else:
                result += str(random.randint(0, 10))
        return result

    def generate_login(user):
        for key in user:
            if key == "f_name":
                login_f = user[key][0:1].lower()
            elif key == "l_name":
                login_l = user[key][0:4].lower()
        return login_f + login_l + str(random.randint(10, 100))

    result['login'] = generate_login(result)
    result['password'] = generate_password()
    result['email'] = result['login'] + '@' + result['email']

    return result


def generate_users(count):
    result = []
    for i in range(count):
        result.append(
            generate_user(f_name=f_name, l_name=l_name, email=email, role_id=role_id, reg_date=reg_date, status=status))
    return result


def generate_workers(count):
    result = []
    for i in range(count):
        result.append(
            generate_user(f_name=f_name, l_name=l_name, email=email, role_id=role_id, reg_date=reg_date))
    return result

####################################
#########      Creating class
####################################
class Write(object):
    def __init__(self, user=None, 
        host=None, passwd=None, db=None):

        try:
            self.connection = mysql.connect(
                user=user,
                host=host,
                passwd=passwd,
                db=db)

            self.cursor = self.connection.cursor()
        except mysql.Error as e:
            print "Error: {}".format(e)

    def execute(self, table=None, data=None):
        row = ",".join(data[0].keys())
        for i in range(len(data)):
            temp = "'" + "','".join(data[i - 1].values()) + "'"
            try:
                self.cursor.execute("INSERT INTO " + table + "(" + row + ") VALUES(" + temp + ")")
                self.connection.commit()
            except mysql.Error as e:
                print "Error in table: {table}: {e}".format(table=table, e=e)

    def close_connection(self):
        self.connection.close()

####################################
#########      Writing to library
####################################
roles = [{'name': 'librarian'}, 
         {'name': 'security'}, 
         {'name': 'manager'},
         {'name': 'somebody'}]

category = [{'name': 'Business'},
            {'name': 'Cumputer Science'},
            {'name': 'Design'},
            {'name': 'Mathematics'},
            {'name': 'Science'}
            ]

subject = [{'name': 'Marketing', 'category_id': '1'},
           {'name': 'AI', 'category_id': '2'},
           {'name': '3D Models', 'category_id': '3'},
           {'name': 'Factorials', 'category_id': '4'},
           {'name': 'Magnetism', 'category_id': '5'}
           ]

books_authors = [{'name': 'Sid van Riel'},
                 {'name': 'Chris Benetton'},
                 {'name': 'Tomas Heardfield'}
                 ]

library_books = [
    {'subject_id': '1', 'author_id': '1', 'title': 'How to become rich using a beer bottle caps', 'amount': '80'},
    {'subject_id': '3', 'author_id': '2', 'title': 'Learning Python in 7 days', 'amount': '100'},
    {'subject_id': '2', 'author_id': '3', 'title': 'Cooking Cake for 5$', 'amount': '50'},
    {'subject_id': '4', 'author_id': '1', 'title': 'Become Proffesional Chess Player in 5 minutes', 'amount': '1'}
    ]

readers = [{'f_name': 'Alan', 'l_name': 'Watts', 'reg_date': time.strftime('%Y-%m-%d %H:%M:%S'), 'reg_period': '365'},
           {'f_name': 'Konan', 'l_name': 'Varvar', 'reg_date': time.strftime('%Y-%m-%d %H:%M:%S'), 'reg_period': '365'},
           {'f_name': 'Bruce', 'l_name': 'Lee', 'reg_date': time.strftime('%Y-%m-%d %H:%M:%S'), 'reg_period': '365'}
           ]

books_monitor = [{'book_id': '1',
                  'worker_id': '1',
                  'reader_id': '1',
                  'issue_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                  'return_date': time.strftime('%Y-%m-%d %H:%M:%S')},
                  {'book_id': '1',
                  'worker_id': '1',
                  'reader_id': '1',
                  'issue_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                  'return_date': time.strftime('%Y-%m-%d %H:%M:%S')},
                  {'book_id': '1',
                  'worker_id': '1',
                  'reader_id': '1',
                  'issue_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                  'return_date': time.strftime('%Y-%m-%d %H:%M:%S')},
                  {'book_id': '1',
                  'worker_id': '1',
                  'reader_id': '1',
                  'issue_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                  'return_date': time.strftime('%Y-%m-%d %H:%M:%S')},]

library = Write(user='root', 
    host='localhost', 
    passwd='',
    db='library_db')

library.execute(table='roles', data=roles)
library.execute(table='category', data=category)
library.execute(table='subject', data=subject)
library.execute(table='workers', data=generate_workers(10))
library.execute(table='books_authors', data=books_authors)
library.execute(table='library_books', data=library_books)
library.execute(table='readers', data=readers)
library.execute(table='books_monitor', data=books_monitor)
library.close_connection()

####################################
#########      Writing to courses
####################################
roles = [{'name': 'administrator'},
         {'name': 'student'},
         {'name': 'moderator'},
         {'name': 'librarian'},
         {'name': 'guest'}]


entity_type = [{'name': 'course'},
               {'name': 'lection'},
               {'name': 'test'}]

courses_difficulty = [{'name': 'BEGINNER'},
                      {'name': 'INTERMEDIATE'},
                      {'name': 'ADVANCED'},
                      {'name': 'GOD'}]

courses = [{'subject_id': '1',
            'author_id': '1',
            'difficulty_id': '1',
            'entity_type_id': '1',
            'name': 'Introduction to Aerodynamics',
            'description': description_4p,
            'status': '1',
            'has_test': '1',
            'test_id': '1'},
           {'subject_id': '2',
            'author_id': '2',
            'difficulty_id': '2',
            'entity_type_id': '2',
            'name': 'Learning From Data',
            'description': description_2p,
            'status': '1',
            'has_test': '1',
            'test_id': '1'},
           {'subject_id': '3',
            'author_id': '3',
            'difficulty_id': '3',
            'entity_type_id': '3',
            'name': 'Software as a Service',
            'description': description_4p,
            'status': '1',
            'has_test': '1',
            'test_id': '1'},
           {'subject_id': '3',
            'author_id': '3',
            'difficulty_id': '3',
            'entity_type_id': '3',
            'name': 'Electricity & Magnetism',
            'description': description_4p,
            'status': '1',
            'has_test': '1',
            'test_id': '1'}]

lectures = [{'course_id': '1',
            'entity_type_id': '1',
            'title': get_words(3),
            'body': description_1p,
            'status': '1',
            'has_test': '1'},
            {'course_id': '1',
            'entity_type_id': '1',
            'title': get_words(3),
            'body': description_1p,
            'status': '1',
            'has_test': '1'},
            {'course_id': '1',
            'entity_type_id': '1',
            'title': get_words(3),
            'body': description_1p,
            'status': '1',
            'has_test': '1'},]

comments = [{'user_id': '1',
            'creation_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'title': get_words(3),
            'body': description_1p,
            'parent_type': '1',
            'parent_id': '1',
            'status': '1'},
            {'user_id': '1',
            'creation_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'title': get_words(3),
            'body': description_1p,
            'parent_type': '1',
            'parent_id': '1',
            'status': '1'},
            {'user_id': '1',
            'creation_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'title': get_words(3),
            'body': description_1p,
            'parent_type': '1',
            'parent_id': '1',
            'status': '1'}]

course_subscriptions = [{'user_id': '1',
                         'course_id': '1',
                         'status': '1',
                         'subscription_date': time.strftime('%Y-%m-%d %H:%M:%S')},
                         {'user_id': '1',
                         'course_id': '1',
                         'status': '1',
                         'subscription_date': time.strftime('%Y-%m-%d %H:%M:%S')},
                         {'user_id': '1',
                         'course_id': '1',
                         'status': '1',
                         'subscription_date': time.strftime('%Y-%m-%d %H:%M:%S')},]

tests = [{'entity_type_id': '1',
          'name': get_words(3),
          'description': description_1p,
          'questions_amount': '1',
          'status': '1'},
          {'entity_type_id': '1',
          'name': get_words(3),
          'description': description_1p,
          'questions_amount': '1',
          'status': '1'},
          {'entity_type_id': '1',
          'name': get_words(3),
          'description': description_1p,
          'questions_amount': '1',
          'status': '1'},]

grades = [{'subscription_id': '1',
           'test_id': '1',
           'test_score': '1',
           'attempt': '1',
           'date': time.strftime('%Y-%m-%d %H:%M:%S'),
           'is_hidden': '1'},
           {'subscription_id': '1',
           'test_id': '1',
           'test_score': '1',
           'attempt': '1',
           'date': time.strftime('%Y-%m-%d %H:%M:%S'),
           'is_hidden': '1'},
           {'subscription_id': '1',
           'test_id': '1',
           'test_score': '1',
           'attempt': '1',
           'date': time.strftime('%Y-%m-%d %H:%M:%S'),
           'is_hidden': '1'},]

test_questions = [{'test_id': '1',
                   'book_id': '1',
                   'question_text': description_1p,
                   'book_details': description_1p},
                   {'test_id': '1',
                   'book_id': '1',
                   'question_text': description_1p,
                   'book_details': description_1p},
                   {'test_id': '1',
                   'book_id': '1',
                   'question_text': description_1p,
                   'book_details': description_1p},]

grade_details = [{'grade_id': '1',
                  'question_id': '1',
                  'question_result': '1'},
                  {'grade_id': '2',
                  'question_id': '2',
                  'question_result': '2'},
                  {'grade_id': '3',
                  'question_id': '3',
                  'question_result': '3'},
                  {'grade_id': '1',
                  'question_id': '1',
                  'question_result': '1'},]

lecture_books = [{'lecture_id': '1',
                  'book_id': '1',
                  'book_details': description_1p},
                  {'lecture_id': '1',
                  'book_id': '1',
                  'book_details': description_1p},
                  {'lecture_id': '1',
                  'book_id': '1',
                  'book_details': description_1p},]

rating = [{'entity_type_id': '1',
           'entity_id': '1',
           'course_average_rating': '1',
           'votes_count': '1'},
           {'entity_type_id': '1',
           'entity_id': '1',
           'course_average_rating': '1',
           'votes_count': '1'},
           {'entity_type_id': '1',
           'entity_id': '1',
           'course_average_rating': '1',
           'votes_count': '1'},]

rating_details = [{'user_id': '1',
                   'rating_id': '1',
                   'details': '1'},
                   {'user_id': '1',
                   'rating_id': '1',
                   'details': '1'},
                   {'user_id': '1',
                   'rating_id': '1',
                   'details': '1'},]

test_answers = [{'question_id': '1',
                 'answer': get_words(5),
                 'is_correct': '1'},
                 {'question_id': '1',
                 'answer': get_words(5),
                 'is_correct': '1'},
                 {'question_id': '1',
                 'answer': get_words(5),
                 'is_correct': '1'},]

course = Write(user='root', 
    host='localhost', 
    passwd='',
    db='courses_db')

course.execute(table='roles', data=roles)
course.execute(table="users", data=generate_users(15))
course.execute(table='entity_type', data=entity_type)
course.execute(table='category', data=category)
course.execute(table='subject', data=subject)
course.execute(table='courses_difficulty', data=courses_difficulty)
course.execute(table='courses', data=courses)
course.execute(table='lectures', data=lectures)
course.execute(table='comments', data=comments)
course.execute(table='course_subscriptions', data=course_subscriptions)
course.execute(table='tests', data=tests)
course.execute(table='grades', data=grades)
course.execute(table='test_questions', data=test_questions)
course.execute(table='grade_details', data=grade_details)
course.execute(table='lecture_books', data=lecture_books)
course.execute(table='rating', data=rating)
course.execute(table='rating_details', data=rating_details)
course.execute(table='test_answers', data=test_answers)

course.close_connection()


