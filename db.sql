CREATE DATABASE IF NOT EXISTS library_db
DEFAULT CHARACTER SET utf8;
    
use library_db;
    
CREATE TABLE category (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL);

CREATE TABLE subject (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    categoryID INT(4) NOT NULL);

CREATE TABLE book_authors (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL);

CREATE TABLE library_books (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    subjectID INT(4) NOT NULL,
    authorID INT(4) NOT NULL,
    title VARCHAR(128) NOT NULL,
    amount INT(4) NOT NULL);

CREATE TABLE roles (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL);

CREATE TABLE workers (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    roleID INT(4) NOT NULL,
    fName VARCHAR(64) NOT NULL,
    lName VARCHAR(64) NOT NULL,
    login VARCHAR(64) NOT NULL,
    password VARCHAR(20) NOT NULL);

CREATE TABLE readers (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fName VARCHAR(64) NOT NULL,
    lName VARCHAR(64) NOT NULL,
    reg_date date NOT NULL,
    reg_period INT(4) NOT NULL);

CREATE TABLE books_monitor (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    bookID INT(4) NOT NULL,
    workerID INT(4) NOT NULL,
    readerID INT(4) NOT NULL,
    issue_date date NOT NULL,
    return_date date NOT NULL);

ALTER TABLE `subject`
ADD FOREIGN KEY(`categoryID`) REFERENCES `category`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `library_books`
ADD FOREIGN KEY(`subjectID`) REFERENCES `subject`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ADD FOREIGN KEY(`authorID`) REFERENCES `book_authors`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `workers`
ADD FOREIGN KEY(`roleID`) REFERENCES `roles`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `books_monitor`
ADD FOREIGN KEY(`bookID`) REFERENCES `library_books`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ADD FOREIGN KEY(`workerID`) REFERENCES `workers`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ADD FOREIGN KEY(`readerID`) REFERENCES `readers`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;



CREATE DATABASE IF NOT EXISTS tests
DEFAULT CHARACTER SET utf8;
    
use tests;
    
CREATE TABLE users (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    roleID INT(4) NOT NULL,
    fName VARCHAR(64) NOT NULL,
    lName VARCHAR(64) NOT NULL,
    login VARCHAR(64) NOT NULL,
    password VARCHAR(20) NOT NULL,
    pass_salt CHAR(20)
    email VARCHAR(64) NOT NULL,
    status TINYINT(4) NOT NULL
);
CREATE TABLE roles (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL
);
CREATE TABLE courses_subscriptions (
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userID INT(4) NOT NULL,
    courseID INT(4) NOT NULL,
    subscription_status TINYINT(2) NOT NULL,
    subscription_date DATE NOT NULL
    );
CREATE TABLE comments(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userID INT(4) NOT NULL,
    creation_date DATE NOT NULL,
    coment_title VARCHAR(64), 
    comment_body VARCHAR(2000) NOT NULL,
    parent_type TINYINT(2) NOT NULL,
    parent_id INT(4) NOT NULL,
    status TINYINT(2) NOT NULL
    );
CREATE TABLE grades(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    subscriptionID INT(4) NOT NULL,
    testID INT(4) NOT NULL,
    test_score INT(4) NOT NULL,
    test_attempt TINYINT(4) NOT NULL,
    test_date DATE NOT NULL,
    is_hidden TINYINT(1) NOT NULL
    );
CREATE TABLE grades_details(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    questionID INT(4) NOT NULL,
    question_result TINYINT(2) NOT NULL,
    gradeID INT(4) NOT NULL
    );
CREATE TABLE tests(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    questions_number INT(4),
    status TINYINT(2),
    entity_typeID INT(4) NOT NULL,
    description VARCHAR (400)
    );
CREATE TABLE test_questions(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    testID INT(4) NOT NULL,
    question_text VARCHAR(64) NOT NULL,
    bookID INT(4),
    book_details VARCHAR(64)
);
CREATE TABLE test_answers(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    questionID INT(4) NOT NULL,
    answer VARCHAR(64) NOT NULL,
    is_correct TINYINT(1) DEFAULT 0 NOT NULL
);
CREATE TABLE category(
    library_categoryID INT(4) NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL
);

CREATE TABLE subject(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    library_categoryID INT(4) NOT NULL
);

CREATE TABLE book_authors(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(80) NOT NULL
);

CREATE TABLE courses(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    library_subjectID INT(4) NOT NULL,
    authorID INT(4) NOT NULL,
    difficultyID INT(4) NOT NULL,
    description VARCHAR(2000) NOT NULL,
    status TINYINT(4) NOT NULL,
    entity_typeID INT(4) NOT NULL,
    has_test TINYINT(1) NOT NULL,
    testID INT(4) 
);
CREATE TABLE course_difficulty(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL
);
CREATE TABLE lectures(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(128) NOT NULL, 
    lecture_body VARCHAR(10000) NOT NULL,
    courseID INT(4) NOT NULL,
    has_test TINYINT(1) NOT NULL,
    testID INT(4),
    status TINYINT(2) NOT NULL,
    entity_typeID INT(4) NOT NULL
);
CREATE TABLE lecture_books(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    lectureID INT(4) NOT NULL,
    bookID INT(4) NOT NULL,
    book_details VARCHAR(128)
);
CREATE TABLE raiting(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    entity_typeID INT(4) NOT NULL,
    entityID INT(4) NOT NULL,
    average_raiting SMALLINT(4),
    votes_count INT(4)
);
CREATE TABLE raiting_details(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userID INT(4),
    raitingID INT(4),
    details VARCHAR(64)
);
CREATE TABLE entity_types(
    id INT(4) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name INT(4) NOT NULL
);

ALTER TABLE `users`
ADD FOREIGN KEY(`roleID`) REFERENCES `roles`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `courses_subscriptions`
ADD FOREIGN KEY(`userID`) REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`courseID`) REFERENCES `courses`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `comments`
ADD FOREIGN KEY(`userID`) REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `grades`
ADD FOREIGN KEY(`subscriptionID`) REFERENCES `courses_subscriptions`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`testID`) REFERENCES `tests`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `grades_details`
ADD FOREIGN KEY(`gradeID`) REFERENCES `grades`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`questionID`) REFERENCES `test_questions`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `tests`
ADD FOREIGN KEY(`entity_typeID`) REFERENCES `entity_types`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `test_questions`
ADD FOREIGN KEY(`testID`) REFERENCES `tests`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ADD FOREIGN KEY(`bookID`) REFERENCES `library_db.library_books`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `test_answers`
ADD FOREIGN KEY(`questionID`) REFERENCES `test_questions`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `subject`
ADD FOREIGN KEY(`library_categoryID`) REFERENCES `category`(`library_categoryID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `lectures`
ADD FOREIGN KEY(`courseID`) REFERENCES `courses`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`testID`) REFERENCES `courses`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`entity_typeID`) REFERENCES `entity_types`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `lecture_books`
ADD FOREIGN KEY(`lectureID`) REFERENCES `lectures`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `raiting`
ADD FOREIGN KEY(`entity_typeID`) REFERENCES `entity_types`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`entityID`) REFERENCES `entity_types`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `raiting_details`
ADD FOREIGN KEY(`userID`) REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`raitingID`) REFERENCES `raiting`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `courses`
ADD FOREIGN KEY(`library_subjectID`) REFERENCES `subject`(`library_subjectID`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`authorID`) REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`difficultyID`) REFERENCES `course_difficulty`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY(`entity_typeID`) REFERENCES `entity_types`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ADD FOREIGN KEY(`testID`) REFERENCES `tests`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*create user 'librarian'@'localhost' identified by 'lu6574hlrt';
grant insert, update, delete, select, create view on library_db.* to 'librarian'@'localhost';

create user 'courses_master'@'localhost' identified by 'ytmktm867';
grant insert, update, delete, select, create view on courses_db.* to 'courses_master'@'localhost';
grant select on library_db.category to 'courses_master'@'localhost';
grant select on library_db.subject to 'courses_master'@'localhost';
grant select on library_db.library_books to 'courses_master'@'localhost';*/
