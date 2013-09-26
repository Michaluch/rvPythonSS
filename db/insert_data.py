#!/usr/bin/env python

import data_insertion
import datetime

db = data_insertion.DataInsertion()
db.connection('localhost', 'librarian', 'lu6574hlrt', 'library_db')


r = [[1, 'administrator'],
    [2, 'moderator'],
    [3, 'librarian']]
db.insert_item('roles', ['id', 'name'], r)
    
    
r = [[1, 'Mykola', 'Melnychuk', 'mymel', '123456', 1],
    [2, 'Vasyl', 'Kvach', 'vasia', '123456', 2],
    [3, 'Serhiy', 'Molodojenia', 'semol', '123456', 3]]
db.insert_item('workers', ['id', 'f_name', 'l_name', 'login', 'password', 'role_id'], r)
    
    
r = [[1, 'Stepan', 'Avramenko', datetime.datetime(2013, 8, 10, 8, 10, 2).strftime('%Y%m%d%H%M%S'), 1],
    [2, 'Yuriy', 'Istomin', datetime.datetime(2013, 7, 10, 8, 10, 2).strftime('%Y%m%d%H%M%S'), 2],
    [3, 'Ivanna', 'Oleksiychuk', datetime.datetime(2013, 6, 10, 8, 10, 2).strftime('%Y%m%d%H%M%S'), 3]]
db.insert_item('readers', ['id', 'f_name', 'l_name', 'reg_date', 'reg_period'], r)

r = [[1, 'Languages'], [2, 'Economy'], [3, 'Mathematics'], [4, 'Programming']]
db.insert_item('category',['id', 'name'], r)

r = [(1, 'English', 1),
    (2, 'Marketing', 2),
    (3, 'Vectors', 3),
    (4, 'Python', 4)]
db.insert_item('subject',['id', 'name', 'category_id'], r)


r = [[1,'Johnson'],
    [2,'Longbotom'],
    [3, 'Kotler'],
    [4, 'Martins'],
    [5, 'Bevs'],
    [6, 'Kramarenko']]
db.insert_item('books_authors', ['id', 'name'], r)
    
 
r = [[1, 'Presetn Simple', 1, 5, 1],
    [2, 'English Grammar Basic', 2, 3, 1],
    [3, 'Marketing in countries', 3, 7, 2],
    [4, 'Market analisys', 4, 10, 2],
    [5, 'Algebra for students', 5, 20, 3],
    [6, 'Vectors in digits', 6, 2, 3]]
db.insert_item('library_books', ['id', 'title', 'author_id', 'amount', 'subject_id'], r)
    

        
r = [[1, datetime.datetime(2013, 8, 10, 8, 10, 2).strftime('%Y%m%d%H%M%S'), datetime.datetime(2013, 1, 1, 1, 1, 1).strftime('%Y%m%d%H%M%S'), 1, 3, 1],
    [2, datetime.datetime(2013, 7, 10, 8, 10, 2).strftime('%Y%m%d%H%M%S'), datetime.datetime(2013, 1, 1, 1, 1, 1).strftime('%Y%m%d%H%M%S'), 3, 3, 2],
    [3, datetime.datetime(2013, 6, 10, 8, 10, 2).strftime('%Y%m%d%H%M%S'), datetime.datetime(2013, 1, 1, 1, 1, 1).strftime('%Y%m%d%H%M%S'), 6, 3, 3]]
db.insert_item('books_monitor', ['id', 'issue_date', 'return_date', 'book_id', 'worker_id', 'reader_id'], r)
   
   
db.close_db()

db = data_insertion.DataInsertion()
db.connection('localhost', 'courses_master', 'ytmktm867', 'courses_db')


r = [[1, 'administrator'],
    [2, 'moderator'],
    [3, 'teacher'],
    [4, 'student']]
db.insert_item('roles',['id', 'name'], r)


r = [[1, 'Dima', 'Melnyk', 'dimel', '123456', '', 1, 'dim@gmail.com', 1],
    [2, 'Kolia', 'Ivanov', 'koliv', '123456', '', 2, 'kol@gmail.com', 1],
    [3, 'Serhiy', 'Kostiuk', 'serko', '123456', '', 3, 'ser@gmail.com', 1],
    [4, 'Ivan', 'Gordiychuk', 'ivgor', '123456', '', 4, 'iva@gmail.com', 1],
    [5, 'Mark', 'Zaychuk', 'mazay', '123456', '', 3, 'mark@gmail.com', 1],
    [6, 'Vadim', 'Tymeychuk', 'vatym', '123456', '', 3, 'vad@gmail.com', 1],
    [7, 'Bohdan', 'Mazuryk', 'bomaz', '123456', '', 4, 'boh@gmail.com', 1],
    [8, 'Andriy', 'Levchuk', 'anlev', '123456', '', 4, 'lev@gmail.com', 1]]
db.insert_item('users', ['id', 'f_name', 'l_name', 'login', 'password', 'pass_salt', 'role_id', 'email', 'status'], r)

r = [[1, 'Languages'],
    [2, 'Economy'],
    [3, 'Mathematics'],
    [4, 'Programming']]
db.insert_item('category',['id', 'name'], r)

r = [[1, 'English', 1],
    [2, 'Marketing', 2],
    [3, 'Vectors', 3],
    [4, 'Python', 4]]
db.insert_item('subject',['id', 'name', 'category_id'], r)


r = [[1, 'basic'],
    [2, 'intermidiate'],
    [3, 'advanced']]
db.insert_item('courses_difficulty',['id', 'name'], r)


r = [[1, 'course'],
    [2, 'test'],
    [3, 'lecture']]
db.insert_item('entity_type',['id', 'name'], r)
    
    
t='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore cu fugiat nulla pariatur.'    
r = [[1, 'English Grammar', 1, t, 1, 3, 1, 1, 0, 0],
    [2, 'Algebra', 1, t, 3, 5, 1, 1, 0, 0],
    [3, 'Polit_econ', 1, t, 2, 6, 1, 1, 1, 3]]
db.insert_item('courses',['id', 'name', 'status', 'description', 'subject_id', 'author_id', 'difficulty_id', 'entity_type_id', 'has_test', 'test_id'], r)


r = [[1, 'English Grammar', 5, 1, 2, ''],
    [2, 'Algebra', 5, 1, 2, ''],
    [3, 'Polit_econ', 5, 1, 2, '']]
db.insert_item('tests', ['id', 'name', 'questions_amount', 'status','entity_type_id', 'description'], r)
    

r = [(1, 'The cars stopped when we were walking _____ the road.', '', 1, 1),
    (2, 'Keep _____ (Do not touch / Do not walk on) the grass!', '', 2, 1),
    (3, 'I am not hungry _____ dinner.', '', 1, 1),
    (4, '"What is the matter _____ you, Peter?" John asked.', '', 2, 1),
    (5, 'I am going on holiday ________ next week.', '', 1, 1),
    (6, 'Which property is displayed in the following equation?    (xy)z = x(yz)', '', 3, 2),
    (7, 'A large pizza has a circumference of 72.5 inches.  Which of the perimeters listed could belong to the smallest box capable of holding a large pizza?', '', 4, 2),
    (8, 'For what values is     undefined?', '', 3, 2),
    (9, 'The ages of two brothers can be represented as consecutive even integers.  If the younger brothers age is x + 3, which expression represents the age of the older brother.', '', 4, 2),
    (10, 'Given the relation A = {(5,2), (7,4), (9,10), (x, 5)}.  Which of the following values for x will make relation A a function?', '', 4, 2),
    (11, 'In economics the central problem is:', '', 5, 3),
    (12, 'Indicate below what is NOT a factor of production.', '', 6, 3),
    (13, 'Macroeconomics deals with:', '', 6, 3),
    (14, 'Microeconomics is not concerned with the behaviour of:', '', 5, 3),
    (15, 'The study of inflation is part of :', '', 5, 3)]
db.insert_item('test_questions',['id', 'question_text', 'book_details', 'book_id', 'test_id'], r)
        
        
r = [(1, 'across', 1, 1),
    (2, 'besides', 0, 1),
    (3, 'between', 0, 1),
    (4, 'about', 0, 1),
    (5, 'over', 0, 1),
    (6, 'up', 0, 2),
    (7, 'off', 0, 2),
    (8, 'away', 1, 2),
    (9, 'down', 0, 2),
    (10, 'off', 0, 3),
    (11, 'like', 0, 3),
    (12, 'except', 0, 3),
    (13, 'after', 1, 3),
    (14, 'past', 0, 3),
    (15, 'into', 0, 4),
    (16, 'of', 0, 4),
    (17, 'beneath', 0, 4),
    (18, 'under', 0, 4),
    (19, 'with', 1, 4),
    (20, 'X', 1, 5),
    (21, 'at', 0, 5),
    (22, 'in', 0, 5),
    (23, 'commutative property of multiplication', 0, 6),
    (24, 'distributive property', 0, 6),
    (25, 'associative property of multiplication', 0, 6),
    (26, 'multiplicative inverse property', 1, 6),
    (27, '23', 0, 7),
    (28, '24', 0, 7),
    (29, '73', 0, 7),
    (30, '96', 1, 7),
    (31, '{2, -7}', 0, 8),
    (32, '{-2, 7}', 1, 8),
    (33, '{2, 7}', 0, 8),
    (34, '{-2, -7}', 0, 8),
    (35, 'x + 1', 1, 9),
    (36, 'x + 4', 0, 9),
    (37, 'x + 5', 0, 9),
    (38, '2x + 3', 0, 9),
    (39, '9', 0, 10),
    (40, '7', 1, 10),
    (41, '5', 0, 10),
    (42, '4', 0, 10),
    (43, 'allocation', 0, 11),
    (44, 'scarcity', 0, 11),
    (45, 'money', 0, 11),
    (46, 'consumption', 0, 11),
    (47, 'production', 1, 11),
    (48, 'Land', 0, 12),
    (49, 'Labour', 0, 12),
    (50, 'A bank loan', 1, 12),
    (51, 'Capital', 0, 12),
    (52, 'the behaviour of firms', 0, 13),
    (53, 'the activities of individual units', 0, 13),
    (54, 'the behaviour of the electronics industry', 0, 13),
    (55, 'economic aggregates', 1, 13),
    (56, 'aggregate demand', 0, 14),
    (57, 'industries', 1, 14),
    (58, 'firms', 0, 14),
    (59, 'consumers', 0, 14),
    (60, 'macroeconomics', 1, 15),
    (61, 'microeconomics', 0, 15),
    (62, 'descriptive economics', 0, 15),
    (63, 'normative economics', 0, 15)]
db.insert_item('test_answers',['id', 'answer', 'is_correct', 'question_id'], r)



r = [(1, 'Present Continuous', 'The present continuous is used to talk about present \
      situations which we see as short-term or temporary . We use the present simple to \
      talk about present situations which we see as long-term or permanent.\
      In these examples, the action is taking place at the time of speaking.\
      It is raining. Who is Kate talking to on the phone? Look, somebody is trying to steal that mans wallet.\
      I am not looking. My eyes are closed tightly. In these examples, the action is true at the present time \
      but we do not think it will be true in the long term. I am looking for a new apartment. \
      He is thinking about leaving his job. They are considering making an appeal against the judgment. \
      Are you getting enough sleep? In these examples, the action is at a definite point in the future and it has already been arranged.\
      I am meeting her at 6.30. They are not arriving until Tuesday. We are having a special dinner at a top restaurant for all \
      the senior managers. Is not he coming to the dinner?', 1, 1, 1, 1, 3),
    (2, 'Definition of Economics', 'The first thing that we should discuss is the definition of "economics." Economists generally \
     define economics as the study of how individuals and societies use limited resources to satisfy unlimited wants. To see how this \
     concept works, think about your own situation. Do you have enough time available for everything that you wish to do? Can you afford \
     every item that you would like to own? Economists argue that virtually everyone wants more of something. Even the wealthiest \
     individuals in society do not seem to be exempt from this phenomenon. This problem of limited resources and unlimited wants \
     also applies to society as a whole. Can you think of any societies in which all wants are satisfied? Most societies \
     would prefer to have better health care, higher quality education, less poverty, a cleaner environment, etc. Unfortunately, \
     there are not enough resources available to satisfy all of these goals. Thus, economists argue that the fundamental economic \
     problem is scarcity. Since there are not enough resources available to satisfy everyone?s wants, individuals and societies \
     have to choose among available alternatives. An alternative, and equivalent, definition of economics is that economics is the \
     study of how such choices are made.', 0, 1, 0, 3, 3),
    (3, 'Present simple', '''The present simple is used to talk about actions we see as long term or permanent. It is very common and very important.
In these examples, we are talking about regular actions or events.
I drive to work every day.
She does not come very often.
The games usually start at 8.00 in the evening.
What do you usually have for breakfast?
In these examples, we are talking about facts.
Water freezes at 0? C or 32? F.
I have three children.
What does this word mean?
I do not have any of my original teeth left.
In these examples, we are talking about future facts, usually found in a timetable or a chart.
The plane leaves at 5.00 tomorrow morning.
Christmas Day falls on a Sunday this year.
Ramadan does not begin for another 2 weeks.
Does the class begin this week or next?
In these examples, we are talking about our thoughts and feelings at the time of speaking. Notice that, although these feelings can be short-term, we use the present simple and not the present continuous.
I think you are wrong.
She does not want to do it.
They do not agree with us.
Do you understand what I am trying to say.''', 0, 1, 0, 1, 3),
    (4, 'Opportunity Cost', '''The opportunity cost of any alternative is defined as the cost of not selecting the "next-best" alternative. Let is consider a few examples of opportunity cost:
Suppose that you own a building that you use for a retail store. If the next-best use of the building is to rent it to someone else, the opportunity cost of using the business for your business is the rent you could have received. If the next-best use of the building is to sell it to someone else, the annual opportunity cost of using it for your own business is the foregone interest that you could have received (e.g., if the interest rate is 10% and the building is worth $100,000, you give up $10,000 in interest each year by keeping the building, assuming that the value of the building remains constant over the year -- depreciation or appreciation would have to be taken into account if the value of the building changes over time).
The opportunity class of attending college includes:
the cost of tuition, books, and supplies (the costs of room and board only appear if these costs differ from the levels that would have been paid in your next-best alternative),
foregone income (this is usually the largest cost associated with college attendance), and
psychic costs (the stress, anxiety, etc. associated with studying, worrying about grades, etc.).
If you attend a movie, the opportunity cost includes not only the cost of the tickets and transportation, but also the opportunity cost of the time required to view the movie.
When economists discuss the costs and benefits associated with alternative activities, the discussion generally focuses on marginal benefits and marginal costs. The marginal benefit from an activity is the additional benefit associated with a one-unit increase in the level of an activity. Marginal cost is defined as the additional cost associated with a one-unit increase in the level of the activity. Economists assume that individuals attempt to maximize the net benefit associated with each activity.
If marginal benefit exceeds marginal cost, net benefit will increase if the level of the activity rises. Therefore, rational individuals will increase the level of any activity when marginal benefit exceeds marginal costs. On the other hand, if marginal cost exceeds marginal benefit, net benefit rises when the level of the activity is decreased. There is no reason to change the level of an activity (and net benefit is maximized) at the level of an activity at which marginal benefit equals marginal cost.''',
    0, 1, 0, 3, 3),
    (5, 'Graphs and Graphing Utilities', '''There are several kinds of graphs that the TI-82 or TI-83 will do, but they are accessed from the same key. The [y=] key and the [2nd] [y=] or [StatPlot] key. The two major kinds of plots may cause confusion when mixed, so it is best to turn off all unnecessary plots before trying to graph an equation.
To turn off all statistical plots, hit [StatPlot] and choose option 4 - PlotsOff. Hit enter to finish the command.
To turn off a regular plot, one can either hit [Clear] while on an equation, or arrow to the left so that the cursor is on the equal sign, and press enter to toggle the display of that equation.
Graphing Equations with the Calculator
Equations must be solved explicitly for y before being placed into the calculator. In other words, y must be written as a function of x before entering the equation into the calculator.
Sometimes, equations can not be solved for y. Other times, the result is not a function. In this case, you may need two y functions.
x2 + y2 = 16 has the solutions y = + sqrt(16 - x2) and y = - sqrt(16 - x2)
When you solve the above equation, you get two values for y. Put the positive square root in y1and the negative square root in y2. Alternatively, you can specify that y2= -y1. On the TI-82, the y1 variable can be found under [2nd] [Vars] (or [Y-Vars]), Function. On the TI-83, it is found under [Vars], Y-Vars, Function.
Zoom Settings
There are several zoom settings that we will be using in this class.
Standard
The standard zoom setting sets the domain and range to [-10,10] and the scale to 1. If you are not familiar with the interval notation [-10,10], please refer to the preliminary chapter.
When moving the cursor in the standard setting, the x-step is 0.21276596 and the y-step is 0.32258065. These are not "nice" values, and often cause problems when trying to find exact values by tracing. They also cause problems with the graph when there are vertical asymptotes (rational expressions) or at the endpoints of the domain (as was illustrated in class with the circle).''',
    0, 1, 0, 2, 3),
    (6, 'Linear Equations and Modeling', '''Definitions
Equation
A statement that two expressions are equal
Solutions
Values which make the equation true
Identity
An equation which is true for every real number in the domain
Contradiction
An equation which is false for every real number in the domain
Conditional equation
An equation which may be true or false depending on the values of the variables.
Equivalent equations
Equations having the same solution set.
Linear equation in one variable
Equation that can be written as ax+b=0, where a and b are reals and a does not equal zero. If a did equal zero, it would be a constant equation and an identity if b=0 or a contradiction if b?0.
Extraneous solutions
Solutions which satisfy an "equivalent" equation, but not the original equation. They can be introduced by multiplying or dividing by an expression containing a variable. They can also be introduced by applying a non-one-to-one function to both sides (like squaring both sides). You should always check your answer when there is a possibility that you have introduced an extraneous solution.
Mathematical model
An algebraic equation used to solve a problem that occurs in real life.''', 1, 1, 2, 2, 3)]
db.insert_item('lectures', ['id', 'title', 'body', 'has_test', 'status', 'test_id', 'course_id', 'entity_type_id'], r)
    
 
r = [(1, 1, 1, ''),
    (2, 2, 5, ''),
    (3, 3, 2, ''),
    (4, 4, 6, ''),
    (5, 5, 3, ''),
    (6, 6, 4, '')]
db.insert_item('lecture_books', ['id', 'lecture_id', 'book_id', 'book_details'], r)


r = [(1, 1, 9, 1, 1),
    (2, 2, 8.5, 1, 2),
    (3, 3, 7, 1, 3),
    (4, 3, 10, 1, 1),
    (5, 1, 6, 1, 2),
    (6, 5, 8, 1, 3)]
db.insert_item('rating', ['id', 'entity_id', 'course_average_rating', 'votes_count', 'entity_type_id'], r)
    
    
r = [[1, 1, datetime.datetime(2013, 9, 6, 12, 10, 13).strftime('%Y%m%d%H%M%S'), 1, 4],
    [2, 1, datetime.datetime(2013, 9, 7, 12, 10, 13).strftime('%Y%m%d%H%M%S'), 2, 7],
    [3, 1, datetime.datetime(2013, 9, 4, 12, 10, 13).strftime('%Y%m%d%H%M%S'), 3, 8]]
db.insert_item('course_subscriptions', ['id', 'status', 'subscription_date', 'course_id', 'user_id'], r)
 
    
r = [(1, 4, 1, 9),
    (2, 7, 2, 8),
    (3, 4, 3, 7),
    (4, 8, 4, 10),
    (5, 4, 5, 6),
    (6, 8, 1, 8)]
db.insert_item('rating_details', ['id', 'user_id', 'rating_id', 'details'], r)
  
    
r = [[1, 'Great lecture', 'This lecture of economics is really great', 1, datetime.datetime(2013, 9, 10, 12, 10, 13).strftime('%Y%m%d%H%M%S'), 3, 4, 8],
    [2, 'Test of English', 'This test is very good!', 1, datetime.datetime(2013, 9, 12, 14, 10, 13).strftime('%Y%m%d%H%M%S'), 2, 1, 4],
    [3, 'Course', 'I finished it successfully', 1, datetime.datetime(2013, 9, 9, 12, 18, 13).strftime('%Y%m%d%H%M%S'), 1, 2, 7]]
db.insert_item('comments', ['id', 'title', 'body', 'status', 'creation_date', 'parent_type', 'parent_id', 'user_id'], r)
  
        
r = [[1, 0, datetime.datetime(2013, 9, 9, 12, 10, 13).strftime('%Y%m%d%H%M%S'), 1, 1, 5, 1],
    [2, 0, datetime.datetime(2013, 9, 8, 12, 10, 13).strftime('%Y%m%d%H%M%S'), 2, 1, 4, 2],
    [3, 0, datetime.datetime(2013, 9, 7, 12, 10, 13).strftime('%Y%m%d%H%M%S'), 3, 1, 3, 3]]
db.insert_item('grades', ['id', 'is_hidden', 'date', 'subscription_id', 'attempt', 'test_score', 'test_id'], r)
     
     
r = [(1, 1, 1, 1),
    (2, 1, 2, 1),
    (3, 1, 3, 1),
    (4, 1, 4, 1),
    (5, 1, 5, 1),
    (6, 1, 6, 2),
    (7, 0, 7, 2),
    (8, 1, 8, 2),
    (9, 1, 9, 2),
    (10, 1, 10, 2),
    (11, 0, 11, 3),
    (12, 0, 12, 3),
    (13, 1, 13, 3),
    (14, 1, 14, 3),
    (15, 1, 15, 3)]
for book in r:
    db.insert_item('grade_details', ['id', 'question_result', 'question_id', 'grade_id'], r)
    
        
db.close_db()