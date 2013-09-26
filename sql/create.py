import MySQLdb as mysql


course_db = 'courses_db'
library_db = 'library_db'


def check_if_exist():
    connection = mysql.connect(
        user='root',
        host='localhost',
        passwd='')
    cursor = connection.cursor()
    try:
        cursor.execute("DROP DATABASE IF EXISTS `{}`;".format(course_db))
        cursor.execute("DROP DATABASE IF EXISTS `{}`;".format(library_db))
        connection.commit()
        cursor.execute("""
                    CREATE DATABASE `{}`
                    DEFAULT CHARACTER SET utf8;""".format(library_db))
        cursor.execute("""
                    CREATE DATABASE `{}`
                    DEFAULT CHARACTER SET utf8;""".format(course_db))
        connection.commit()
    except mysql.Error, e:
        print 'Error: {}'.format(e)
    finally:
        connection.close()
check_if_exist()


courses_sql = open('{}.sql'.format(course_db), 'r')
library_sql = open('{}.sql'.format(library_db), 'r')

connect_course = mysql.connect(
    user='root',
    host='localhost',
    passwd='',
    db='courses_db')
cursor_course = connect_course.cursor()

connect_library = mysql.connect(
    user='root',
    host='localhost',
    passwd='',
    db='library_db')
cursor_library = connect_library.cursor()


def find_sql(file):
    temp = ''
    f_name = file.name
    for line in file:
        if not len(line) != 1 or not line[0] != '-':
            pass
        else:
            temp += line

        if temp[-2:-1] == ';':
            if f_name[:-4] == library_db:
                cursor_library.execute(temp.strip())
            else:
                cursor_course.execute(temp.strip())
            temp = ''
    connect_library.commit()
find_sql(library_sql)
find_sql(courses_sql)


library_sql.close()
courses_sql.close()

connect_course.close()
connect_library.close()






# def execute_sql(data):
#     for sql in data:
#         # print data[sql]
#         cursor.execute(sql)
#     connection.commit()


# data = ("""create table elearning_test.roles(
#             id int(11) not null auto_increment,
#             name varchar(32) not null,
#             primary key (id))""",
# """create table elearning_test.users(
# id int(11) not null auto_increment,
# fname varchar(32) not null,
# lname varchar(32) not null,
# login varchar(32) not null,
# password char(64) not null,
# reg_date datetime not null,
# role_id int(11) not null,
# email varchar(128) not null,
# is_active tinyint not null,
# primary key (id))""")

# execute_sql(data)
