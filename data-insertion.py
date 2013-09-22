#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = 'alex'

import sys
import MySQLdb as mdb


class insertPosts:

    def __init__(self):
        pass

    def connect_to_db(self, host, user, password, db_name):
        try:
            self.con = mdb.connect(host, user, password, db_name)
            self.con.set_character_set('utf8')
            self.cur = self.con.cursor()
            self.cur.execute('SET NAMES utf8;')
            self.cur.execute('SET CHARACTER SET utf8;')
            self.cur.execute('SET character_set_connection=utf8;')
        except mdb.Error as e:
            print "Problem while connecting to db. Details below: "
            print "Error {0}: {1}".format(e.args[0], e.args[1])
            if self.con:
                self.con.close()
            #sys.exit(1)

    def exec_sql(self, sql, exec_list):
        try:
            self.cur.executemany(sql, exec_list)
            self.con.commit()
        except mdb.Error as e:
            print "Error {0}: {1}".format(e.args[0], e.args[1])
            print sql
            self.con.rollback()
            if self.con:
                self.con.close()
            #sys.exit(1)

#---------------------------
#working with library_db
#---------------------------

ins = insertPosts()

ins.connect_to_db("localhost", "librarian", "lu6574hlrt", "library_db")

roles_sql = "insert into roles (name) values(%s)"
roles_values = [("Супер библиотекарь",),
                ("Библиотекарь",)]
ins.exec_sql(roles_sql, roles_values)

category_sql = "insert into category (name) values (%s)"
category_values = [("Астрономия",),
                   ("Компьютерные науки",)]
ins.exec_sql(category_sql, category_values)

subject_sql = "insert into subject (name, category_id) values (%s, %s)"
subject_values = [("Языки программирования", 2),
                  ("Администрирование ОС", 2),
                  ("Солнечная система", 1),
                  ("Планета Земля", 1)]
ins.exec_sql(subject_sql, subject_values)

workers_sql = "insert into workers (role_id, f_name, l_name, login, password) values (%s, %s, %s, %s, %s)"
workers_values = [(1, "Матвєєв", "Євгеній", "login1", "pass1"),
                  (2, "Ручка", "Ірина", "login2", "pass2"),
                  (2, "Малиш", "Сергій ", "login3", "pass3"),
                  (2, "Зуб", "Наталія", "login4", "pass4")]
ins.exec_sql(workers_sql, workers_values)

books_authors_sql = "insert into books_authors (name) values (%s)"
books_authors_values = [("Eleonora Shah",),
                        ("Ivan Fast",),
                        ("Алан Александер Милн",),
                        ("Александр Веона",),
                        ("Барто Агния Львовна",),
                        ("П. Бляхин",),
                        ("Илья Бражнин",),
                        ("Братья Гримм",),
                        ("Виктор Сидоров",),
                        ("Аркадий Власов Александр; Млодик",)]
ins.exec_sql(books_authors_sql, books_authors_values)

library_books_sql = "insert into library_books (subject_id, author_id, title, amount) values (%s, %s, %s, %s)"
library_books_values = [(1, 1, "Python for tanks", 10),
                        (1, 2, "Pyhton for blonds", 12),
                        (1, 3, "Pyhton for wolfs", 8),
                        (1, 4, "OOP for birds", 3),
                        (1, 5, "C-- for tubes", 21),
                        (2, 6, "Crash Windows in 5 sec", 20),
                        (2, 7, "Doomed MS-DOS", 3),
                        (3, 8, "UFO near Venus", 2),
                        (3, 9, "Asteroid belt", 20),
                        (4, 10, "Earth doomed", 1)]
ins.exec_sql(library_books_sql, library_books_values)

readers_sql = "insert into readers (f_name, l_name, reg_date, reg_period) values (%s, %s, %s, %s)"
readers_values = [("Нил", "Армстронг", "1930-10-20", 864000000),
                  ("Базз", "Олдрин", "1931-01-01", 864000200),
                  ("Пит", "Конрад", "1932-02-02", 864000300),
                  ("Алан", "Бин", "1932-04-06", 864000400),
                  ("Алан", "Шепард", "1923-02-02", 864000500),
                  ("Эдгар", "Митчелл", "1930-07-12", 864000600),
                  ("Дэвид", "Скотт", "1932-06-17", 864000700),
                  ("Джеймс", "Ирвин", "1930-12-31", 864000800),
                  ("Джон", "Янг", "1930-03-08", 864000900),
                  ("Чарльз", "Дьюк", "1935-05-23", 864006000),
                  ("Юджин", "Сернан", "1934-02-20", 864000800),
                  ("Харрисон", "Шмитт", "1935-11-01", 86400700)]
ins.exec_sql(readers_sql, readers_values)

books_monitor_sql = "insert into books_monitor (book_id, worker_id, reader_id, issue_date, return_date) values \
                    (%s, %s, %s, %s, %s)"
books_monitor_values = [(9, 2, 1, "2005-05-01", "2005-06-01"),
                        (9, 3, 12, "2010-01-12", "2010-02-12"),
                        (6, 4, 5, "2008-03-01", "2008-04-01"),
                        (2, 2, 10, "2011-06-13", "2011-07-13"),
                        (9, 3, 6, "2050-06-04", "2050-07-04"),
                        (1, 1, 2, "2000-01-01", "2000-02-01"),
                        (7, 3, 8, "2011-05-05", "2011-06-05"),
                        (8, 3, 5, "2001-09-11", "2001-10-11"),
                        (4, 2, 1, "2006-03-08", "2006-04-08"),
                        (10, 2, 3, "2007-05-03", "2007-06-03")]
ins.exec_sql(books_monitor_sql, books_monitor_values)
ins.con.close()

#---------------------------
#working with courses_db
#---------------------------

ins.connect_to_db("localhost", "courses_master", "ytmktm867", "courses_db")

roles_sql = "insert into roles (name) values (%s)"
roles_values = [("Администратор",),
                ("Учитель",),
                ("Студент",)]
ins.exec_sql(roles_sql, roles_values)

entity_type_sql = "insert into entity_type (name) values (%s)"
entity_type_values = [("Курс",),
                      ("Лекция",),
                      ("Тест",)]
ins.exec_sql(entity_type_sql, entity_type_values)

category_sql = "insert into category (id, name) values (%s, %s)"
category_values = [(1, "Космос"),
                   (2, "Компьютеры")]
ins.exec_sql(category_sql, category_values)

subject_sql = "insert into subject (id, name, category_id) values (%s, %s, %s)"
subject_values = [(1, "Программирование", 2),
                  (2, "Администрирование", 2),
                  (3, "Солнечная система", 1),
                  (4, "Земля", 1)]
ins.exec_sql(subject_sql, subject_values)

courses_difficulty_sql = "insert into courses_difficulty (name) values (%s)"
courses_difficulty_values = [("Легкий",),
                             ("Средний",),
                             ("Сложный",),
                             ("Сумашедший",)]
ins.exec_sql(courses_difficulty_sql, courses_difficulty_values)

users_sql = "insert into users (role_id, f_name, l_name, login, password, pass_salt, email, status) \
            values (%s, %s, %s, %s, %s, %s, %s, %s)"
users_values = [(1, "Администратор", "Админ", "login10", "pass10", "12345678901234567890", "email1@em.inc", 1),
                (2, "Александрр", "Мироненко", "login11", "pass11", "12345678901234567890", "email2@em.inc", 1),
                (2, "Евгений", "Штыков", "login12", "pass12", "12345678901234567890", "email3@em.inc", 1),
                (3, "Путиевский", "Леонид", "login13", "pass13", "12345678901234567890", "email4@em.inc", 1),
                (3, "Александр", "Сергеев", "login14", "pass14", "12345678901234567890", "email5@em.inc", 1),
                (3, "Ступников", "Андрей", "login15", "pass15", "12345678901234567890", "email6@em.inc", 1),
                (3, "Герасименко", "Сергей", "login16", "pass16", "12345678901234567890", "email7@em.inc", 1),
                (3, "Ботов", "Антон", "login17", "pass17", "12345678901234567890", "email8@em.inc", 0),
                (3, "Дмитрий", "Гуркин", "login18", "pass18", "12345678901234567890", "email9@em.inc", 0),
                (3, "Александр", "Лисицын", "login19", "pass19", "12345678901234567890", "email10@em.inc", 0),
                (3, "Дмитрий", "Старков", "login20", "pass20", "12345678901234567890", "email11@em.inc", 0),
                (3, "Алексей", "Мартемьянов", "login21", "pass21", "12345678901234567890", "email12@em.inc", 0),
                (3, "Виктор", "Филимоненков", "login22", "pass22", "12345678901234567890", "email13@em.inc", 0)]
ins.exec_sql(users_sql, users_values)

courses_sql = "insert into courses (subject_id, author_id, difficulty_id, entity_type_id, name, description, \
               status, has_test, test_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
courses_values = [(1, 2, 2, 1, "Программирование на Python", "Для знающих", 1, 1, 1),
                  (3, 3, 1, 1, "Главный пояс астероидов", "Для не знающих", 1, 0, 0)]
ins.exec_sql(courses_sql, courses_values)

lectures_sql = "insert into lectures (course_id, entity_type_id, title, body, status, has_test, test_id) \
               values (%s, %s, %s, %s, %s, %s, %s)"
lectures_values = [(1, 2, "Курс 1 лекция 1", "Длинный длинный длинный нудный текст лекции 1 по курсу 1", 1, 1, 2),
                   (1, 2, "Курс 1 лекция 2", "Длинный длинный длинный нудный текст лекции 2 по курсу 1", 1, 1, 3),
                   (2, 2, "Курс 2 лекция 1", "Длинный длинный длинный нудный текст лекции 1 по курсу 2", 1, 1, 4),
                   (2, 2, "Курс 2 лекция 2", "Длинный длинный длинный нудный текст лекции 2 по курсу 2", 1, 1, 5)]
ins.exec_sql(lectures_sql, lectures_values)

lecture_books_sql = "insert into lecture_books (lecture_id, book_id, book_details) values (%s, %s, %s)"
lecture_book_values = [(1, 1, "глава 1"),
                       (1, 1, "глава 2"),
                       (2, 1, "глава 3"),
                       (2, 1, "глава 4"),
                       (3, 9, "глава 1"),
                       (4, 9, "глава 2")]
ins.exec_sql(lecture_books_sql, lecture_book_values)

tests_sql = "insert into tests (entity_type_id, name, description, questions_amount, status) values(%s, %s, %s, %s, %s)"
tests_values = [(3, "тест к курсу 1", "программироване", 5, 1),
                (3, "тест к лекции 1 курс 1", "программироване", 5, 1),
                (3, "тест к лекции 2 курс 1", "программироване", 5, 1),
                (3, "тест к лекции 1 курс 2", "астероиды", 5, 1),
                (3, "тест к лекции 2 курс 2", "астероиды", 5, 1)]
ins.exec_sql(tests_sql, tests_values)

test_questions_sql = "insert into test_questions (test_id, book_id, question_text, book_details) values (%s, %s, %s, %s)"
test_questions_values = [(1, 1, "текст вопроса 1", "глава 1"),
                         (1, 1, "текст вопроса 2", "глава 2"),
                         (1, 1, "текст вопроса 3", "глава 3"),
                         (1, 1, "текст вопроса 4", "глава 4"),
                         (1, 1, "текст вопроса 5", "глава 5"),
                         (2, 1, "текст вопроса 6", "глава 2 стр 2"),
                         (2, 1, "текст вопроса 7", "глава 2 стр 3"),
                         (2, 1, "текст вопроса 8", "глава 2 стр 4"),
                         (2, 1, "текст вопроса 9", "глава 2 стр 5"),
                         (2, 1, "текст вопроса 10", "глава 2 стр 6"),
                         (3, 1, "текст вопроса 11", "глава 3 стр 2"),
                         (3, 1, "текст вопроса 12", "глава 3 стр 3"),
                         (3, 1, "текст вопроса 13", "глава 3 стр 4"),
                         (3, 1, "текст вопроса 14", "глава 3 стр 5"),
                         (3, 1, "текст вопроса 15", "глава 3 стр 6"),
                         (4, 9, "текст вопроса 16", "глава 1 стр 2"),
                         (4, 9, "текст вопроса 17", "глава 1 стр 3"),
                         (4, 9, "текст вопроса 18", "глава 1 стр 4"),
                         (4, 9, "текст вопроса 19", "глава 1 стр 5"),
                         (4, 9, "текст вопроса 20", "глава 1 стр 6"),
                         (5, 9, "текст вопроса 21", "глава 2 стр 2"),
                         (5, 9, "текст вопроса 22", "глава 2 стр 3"),
                         (5, 9, "текст вопроса 23", "глава 2 стр 4"),
                         (5, 9, "текст вопроса 24", "глава 2 стр 5"),
                         (5, 9, "текст вопроса 25", "глава 2 стр 6")]
ins.exec_sql(test_questions_sql, test_questions_values)

test_answers_sql = "insert into test_answers (question_id, answer, is_correct) values (%s, %s, %s)"
test_answers_values = [(1, "ответ", 1),
                       (1, "ответ", 0),
                       (1, "ответ", 0),
                       (2, "ответ", 1),
                       (2, "ответ", 0),
                       (2, "ответ", 0),
                       (3, "ответ", 1),
                       (3, "ответ", 0),
                       (3, "ответ", 0),
                       (4, "ответ", 1),
                       (4, "ответ", 0),
                       (4, "ответ", 0),
                       (5, "ответ", 1),
                       (5, "ответ", 0),
                       (5, "ответ", 0),
                       (6, "ответ", 1),
                       (6, "ответ", 0),
                       (6, "ответ", 0),
                       (7, "ответ", 1),
                       (7, "ответ", 0),
                       (7, "ответ", 0),
                       (8, "ответ", 1),
                       (8, "ответ", 0),
                       (8, "ответ", 0),
                       (9, "ответ", 1),
                       (9, "ответ", 0),
                       (9, "ответ", 0),
                       (10, "ответ", 1),
                       (10, "ответ", 0),
                       (10, "ответ", 0),
                       (11, "ответ", 1),
                       (11, "ответ", 0),
                       (11, "ответ", 0),
                       (12, "ответ", 1),
                       (12, "ответ", 0),
                       (12, "ответ", 0),
                       (13, "ответ", 1),
                       (13, "ответ", 0),
                       (13, "ответ", 0),
                       (14, "ответ", 1),
                       (14, "ответ", 0),
                       (14, "ответ", 0),
                       (15, "ответ", 1),
                       (15, "ответ", 0),
                       (15, "ответ", 0),
                       (16, "ответ", 1),
                       (16, "ответ", 0),
                       (16, "ответ", 0),
                       (17, "ответ", 1),
                       (17, "ответ", 0),
                       (17, "ответ", 0),
                       (18, "ответ", 1),
                       (18, "ответ", 0),
                       (18, "ответ", 0),
                       (19, "ответ", 1),
                       (19, "ответ", 0),
                       (19, "ответ", 0),
                       (20, "ответ", 1),
                       (20, "ответ", 0),
                       (20, "ответ", 0),
                       (21, "ответ", 1),
                       (21, "ответ", 0),
                       (21, "ответ", 0),
                       (22, "ответ", 1),
                       (22, "ответ", 0),
                       (22, "ответ", 0),
                       (23, "ответ", 1),
                       (23, "ответ", 0),
                       (23, "ответ", 0),
                       (24, "ответ", 1),
                       (24, "ответ", 0),
                       (24, "ответ", 0),
                       (25, "ответ", 1),
                       (25, "ответ", 0),
                       (25, "ответ", 0)]
ins.exec_sql(test_answers_sql, test_answers_values)

course_subscriptions_sql = "insert into course_subscriptions (user_id, course_id, status, subscription_date) \
                           values (%s, %s, %s, %s)"
course_subscriptions_values = [(4, 1, 1, "2011-04-10"),
                               (5, 1, 1, "2011-05-10"),
                               (6, 2, 1, "2011-06-10"),
                               (7, 2, 1, "2011-07-10"),
                               (4, 2, 1, "2011-08-10")]
ins.exec_sql(course_subscriptions_sql, course_subscriptions_values)

grades_sql = "insert into grades (subscription_id, test_id, test_score, attempt, date, is_hidden) \
              values (%s, %s, %s, %s, %s, %s)"
grades_values = [(1, 2, 50, 1, "2012-01-01", 0),
                 (1, 3, 60, 1, "2012-01-02", 0),
                 (1, 1, 71, 1, "2012-01-03", 1),
                 (2, 2, 11, 1, "2012-02-01", 0),
                 (2, 3, 68, 1, "2012-02-02", 0),
                 (3, 4, 27, 1, "2012-03-01", 0),
                 (3, 5, 65, 1, "2012-03-02", 0),
                 (4, 4, 80, 1, "2012-04-01", 0),
                 (4, 5, 91, 1, "2012-04-02", 0),
                 (5, 4, 78, 1, "2012-05-01", 0),
                 (5, 5, 92, 1, "2012-05-02", 0)]
ins.exec_sql(grades_sql, grades_values)

grade_details_sql = "insert into grade_details (grade_id, question_id, question_result) values (%s, %s, %s)"
grade_details_values = [(1, 6, 1),
                        (1, 7, 2),
                        (1, 8, 1),
                        (1, 9, 1),
                        (1, 10, 1),
                        (2, 11, 1),
                        (2, 12, 2),
                        (2, 13, 1),
                        (2, 14, 1),
                        (2, 15, 1),
                        (3, 1, 1),
                        (3, 2, 3),
                        (3, 3, 1),
                        (3, 4, 2),
                        (3, 5, 1),
                        (4, 6, 1),
                        (4, 7, 1),
                        (4, 8, 1),
                        (4, 9, 1),
                        (4, 10, 2),
                        (5, 11, 2),
                        (5, 12, 2),
                        (5, 13, 1),
                        (5, 14, 1),
                        (5, 15, 1),
                        (6, 16, 1),
                        (6, 17, 2),
                        (6, 18, 1),
                        (6, 19, 1),
                        (6, 20, 3),
                        (7, 21, 3),
                        (7, 22, 1),
                        (7, 23, 1),
                        (7, 24, 2),
                        (7, 25, 1),
                        (8, 16, 1),
                        (8, 17, 2),
                        (8, 18, 1),
                        (8, 19, 1),
                        (8, 20, 2),
                        (9, 21, 1),
                        (9, 22, 1),
                        (9, 23, 3),
                        (9, 24, 1),
                        (9, 25, 1),
                        (10, 16, 1),
                        (10, 17, 1),
                        (10, 18, 3),
                        (10, 19, 3),
                        (10, 20, 2),
                        (11, 21, 3),
                        (11, 22, 1),
                        (11, 23, 1),
                        (11, 24, 1),
                        (11, 25, 1)]
ins.exec_sql(grade_details_sql, grade_details_values)

comments_sql = "insert into comments (user_id, creation_date, title, body, parent_type, parent_id, status) values \
                (%s, %s, %s, %s, %s, %s, %s)"
comments_values = [(4, "2012-01-01", "comment title 1", "comment body 1", 1, 5, 1),
                   (5, "2012-02-01", "comment title 2", "comment body 2", 2, 1, 0),
                   (6, "2012-03-01", "comment title 3", "comment body 3", 1, 1, 1),
                   (7, "2012-04-01", "comment title 4", "comment body 4", 2, 2, 1),
                   (4, "2012-05-01", "comment title 5", "comment body 5", 1, 3, 1),
                   (5, "2012-06-01", "comment title 6", "comment body 6", 2, 4, 0),
                   (6, "2012-07-01", "comment title 7", "comment body 7", 1, 2, 1),
                   (7, "2012-08-01", "comment title 8", "comment body 8", 2, 3, 1)]
ins.exec_sql(comments_sql, comments_values)

rating_sql = "insert into rating (entity_type_id, entity_id, course_average_rating, votes_count) values \
              (%s, %s, %s, %s)"
rating_values = [(1, 1, 2, 4),
                 (1, 2, 2, 4),
                 (2, 1, 2, 4),
                 (2, 2, 2, 4),
                 (2, 3, 2, 4),
                 (2, 4, 2, 4),
                 (3, 1, 2, 4),
                 (3, 2, 2, 4),
                 (3, 3, 2, 4),
                 (3, 4, 2, 4),
                 (3, 5, 2, 4)]
ins.exec_sql(rating_sql, rating_values)

rating_details_sql = "insert into rating_details (user_id, rating_id, details) values (%s, %s, %s)"
rating_details_values = [(7, 11, 2),
                         (6, 11, 2),
                         (5, 11, 2),
                         (4, 11, 2),
                         (7, 10, 2),
                         (6, 10, 2),
                         (5, 10, 2),
                         (4, 10, 2),
                         (7, 9, 2),
                         (6, 9, 2),
                         (5, 9, 2),
                         (4, 9, 2),
                         (7, 8, 2),
                         (6, 8, 2),
                         (5, 8, 2),
                         (4, 8, 2),
                         (7, 7, 2),
                         (6, 7, 2),
                         (5, 7, 2),
                         (4, 7, 2),
                         (7, 6, 2),
                         (6, 6, 2),
                         (5, 6, 2),
                         (4, 6, 2),
                         (7, 5, 2),
                         (6, 5, 2),
                         (5, 5, 2),
                         (4, 5, 2),
                         (7, 4, 2),
                         (6, 4, 2),
                         (5, 4, 2),
                         (4, 4, 2),
                         (7, 3, 2),
                         (6, 3, 2),
                         (5, 3, 2),
                         (4, 3, 2),
                         (7, 2, 2),
                         (6, 2, 2),
                         (5, 2, 2),
                         (4, 2, 2),
                         (7, 1, 2),
                         (6, 1, 2),
                         (5, 1, 2),
                         (4, 1, 2)]
ins.exec_sql(rating_details_sql, rating_details_values)
ins.con.close()