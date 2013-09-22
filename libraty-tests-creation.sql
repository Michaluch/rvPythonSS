create database if not exists library_db
  default character set utf8 collate utf8_general_ci;

use library_db;

set foreign_key_checks = 0;

create table if not exists category(
  id int unsigned auto_increment,
  name varchar(80) not null,
  primary key (id)
);

create table if not exists subject(
  id int unsigned auto_increment,
  name varchar(80) not null,
  category_id int unsigned not null,
  primary key (id),
  foreign key fk_category(category_id)
  references category(id)
  on delete cascade
  on update cascade
);

create table if not exists books_authors(
  id int unsigned auto_increment,
  name varchar(90) not null,
  primary key (id)
);

create table if not exists library_books(
  id int unsigned auto_increment,
  subject_id int unsigned not null,
  author_id int unsigned not null,
  title varchar(120) not null,
  amount int unsigned not null,
  primary key (id),
  foreign key fk_subject(subject_id)
  references subject(id)
  on delete cascade
  on update cascade,
  foreign key fk_author(author_id)
  references books_authors(id)
  on delete cascade
  on update cascade
);

create table if not exists roles(
  id int unsigned auto_increment,
  name varchar(50) not null,
  primary key (id)
);

create table if not exists workers(
  id int unsigned auto_increment,
  role_id int unsigned not null,
  f_name varchar(50) not null,
  l_name varchar(50) not null,
  login varchar(20) not null,
  password varchar(20) not null,
  primary key (id),
  foreign key fk_role(role_id)
  references roles(id)
  on delete cascade
  on update cascade
);

create table if not exists readers(
  id int unsigned auto_increment,
  f_name varchar(50) not null,
  l_name varchar(50) not null,
  reg_date date not null,
  reg_period int unsigned not null,
  primary key (id)
);

create table if not exists books_monitor(
  id int unsigned auto_increment,
  book_id int unsigned not null,
  worker_id int unsigned not null,
  reader_id int unsigned not null,
  issue_date date not null,
  return_date date not null,
  primary key (id),
  foreign key fk_book(book_id)
  references library_books(id)
  on delete cascade
  on update cascade,
  foreign key fk_worker(worker_id)
  references workers(id)
  on delete cascade
  on update cascade,
  foreign key fk_reader(reader_id)
  references readers(id)
  on delete no action
  on update cascade
);

/*------------------------------------------
courses_db
------------------------------------------*/

create database if not exists courses_db
  default character set utf8 collate utf8_general_ci;

use courses_db;

set foreign_key_checks = 0;

create table if not exists roles(
  id int unsigned auto_increment,
  name varchar(50) not null,
  primary key (id)
);

create table if not exists users(
  id int unsigned auto_increment,
  role_id int unsigned not null,
  f_name varchar(50) not null,
  l_name varchar(50) not null,
  login varchar(20) not null,
  password varchar(20) not null,
  pass_salt char(20) not null,
  email varchar(20) not null,
  status tinyint(4) not null,
  primary key (id),
  foreign key fk_role(role_id)
  references roles(id)
  on delete cascade
  on update cascade
);

create table if not exists category(
  id int unsigned not null,
  name varchar(80) not null,
  primary key (id),
  foreign key fk_library_category(id)
  references library_db.category(id)
  on delete no action
  on update cascade
);

create table if not exists subject(
  id int unsigned not null,
  name varchar(80) not null,
  category_id int unsigned not null,
  primary key (id),
  foreign key fk_library_subject(id)
  references library_db.subject(id)
  on delete no action
  on update cascade,
  foreign key fk_category(category_id)
  references category(id)
  on delete cascade
  on update cascade
);

create table if not exists courses_difficulty(
  id int unsigned auto_increment,
  name varchar(60) not null,
  primary key (id)
);

create table if not exists entity_type(
  id int unsigned auto_increment,
  name varchar(60) not null,
  primary key (id)
);

create table if not exists courses(
  id int unsigned auto_increment,
  subject_id int unsigned not null,
  author_id int unsigned not null,
  difficulty_id int unsigned not null,
  entity_type_id int unsigned not null,
  name varchar(120) not null,
  description varchar(400) not null,
  status tinyint(2) unsigned not null,
  has_test tinyint(1) unsigned not null,
  test_id int unsigned,
  primary key (id),
  foreign key fk_subject(subject_id)
  references subject(id)
  on delete cascade
  on update cascade,
  foreign key fk_author(author_id)
  references users(id)
  on delete cascade
  on update cascade,
  foreign key fk_difficulty(difficulty_id)
  references courses_difficulty(id)
  on delete no action
  on update cascade,
  foreign key fk_entity_type(entity_type_id)
  references entity_type(id)
  on delete no action
  on update cascade
);

create table if not exists course_subscriptions(
  id int unsigned auto_increment,
  user_id int unsigned not null,
  course_id int unsigned not null,
  status tinyint(2) unsigned not null,
  subscription_date date not null,
  primary key (id),
  foreign key fk_user(user_id)
  references users(id)
  on delete cascade
  on update cascade,
  foreign key fk_course(course_id)
  references courses(id)
  on delete no action
  on update cascade
);

create table if not exists lectures(
  id int unsigned auto_increment,
  course_id int unsigned not null,
  entity_type_id int unsigned not null,
  title varchar(200) not null,
  body varchar(10000) not null,
  status tinyint(2) unsigned not null,
  has_test tinyint(1) unsigned not null,
  test_id int unsigned,
  primary key (id),
  foreign key fk_course(course_id)
  references courses(id)
  on delete cascade
  on update cascade,
  foreign key fk_entity_type(entity_type_id)
  references entity_type(id)
  on delete no action
  on update cascade
);

create table if not exists lecture_books(
  id int unsigned auto_increment,
  lecture_id int unsigned not null,
  book_id int unsigned not null,
  book_details varchar(200),
  primary key (id),
  foreign key fk_lecture(lecture_id)
  references lectures(id)
  on delete cascade
  on update cascade,
  foreign key fk_book(book_id)
  references library_db.library_books(id)
  on delete cascade
  on update cascade
);

create table if not exists rating(
  id int unsigned auto_increment,
  entity_type_id int unsigned not null,
  entity_id int unsigned not null,
  course_average_rating smallint unsigned not null,
  votes_count int unsigned not null,
  primary key (id),
  foreign key fk_entity_type(entity_type_id)
  references entity_type(id)
  on delete no action
  on update cascade
);

create table if not exists rating_details(
  id int unsigned auto_increment,
  user_id int unsigned not null,
  rating_id int unsigned not null,
  details smallint unsigned not null,
  primary key (id),
  foreign key fk_user(user_id)
  references users(id)
  on delete cascade
  on update cascade,
  foreign key fk_rating(rating_id)
  references rating(id)
  on delete cascade
  on update cascade
);

create table if not exists tests(
  id int unsigned auto_increment,
  entity_type_id int unsigned not null,
  name varchar(120) not null,
  description varchar(400) not null,
  questions_amount tinyint unsigned not null,
  status tinyint(2) unsigned not null,
  primary key (id),
  foreign key fk_entity_type(entity_type_id)
  references entity_type(id)
  on delete no action
  on update cascade
);

create table if not exists test_questions(
  id int unsigned auto_increment,
  test_id int unsigned not null,
  book_id int unsigned not null,
  question_text varchar(300) not null,
  book_details varchar(200) not null,
  primary key (id),
  foreign key fk_test(test_id)
  references tests(id)
  on delete cascade
  on update cascade,
  foreign key fk_book(book_id)
  references library_db.library_books(id)
  on delete no action
  on update cascade
);

create table if not exists test_answers(
  id int unsigned auto_increment,
  question_id int unsigned not null,
  answer varchar(300) not null,
  is_correct tinyint(1) unsigned default 0 not null,
  primary key (id),
  foreign key fk_question(question_id)
  references test_questions(id)
  on delete cascade
  on update cascade
);

create table if not exists grades(
  id int unsigned auto_increment,
  subscription_id int unsigned not null,
  test_id int unsigned not null,
  test_score smallint unsigned not null,
  attempt tinyint unsigned not null,
  date date not null,
  is_hidden tinyint(1) unsigned not null,
  primary key (id),
  foreign key fk_subscription(subscription_id)
  references course_subscriptions(id)
  on delete cascade
  on update cascade,
  foreign key fk_test(test_id)
  references tests(id)
  on delete cascade
  on update cascade
);

create table if not exists grade_details(
  id int unsigned auto_increment,
  grade_id int unsigned not null,
  question_id int unsigned not null,
  question_result tinyint(2) unsigned not null,
  primary key (id),
  foreign key fk_grades(grade_id)
  references grades(id)
  on delete cascade
  on update cascade,
  foreign key fk_question(question_id)
  references test_questions(id)
  on delete cascade
  on update cascade
);

create table if not exists comments(
  id int unsigned auto_increment,
  user_id int unsigned not null,
  creation_date datetime not null,
  title varchar(70) not null,
  body varchar(500) not null,
  parent_type tinyint(2) unsigned not null,
  parent_id int unsigned not null,
  status tinyint(2) unsigned not null,
  primary key (id),
  foreign key fk_user(user_id)
  references users(id)
  on delete cascade
  on update cascade
);

/*create user 'librarian'@'localhost' identified by 'lu6574hlrt';
grant insert, update, delete, select, create view on library_db.* to 'librarian'@'localhost';

create user 'courses_master'@'localhost' identified by 'ytmktm867';
grant insert, update, delete, select, create view on courses_db.* to 'courses_master'@'localhost';
grant select on library_db.category to 'courses_master'@'localhost';
grant select on library_db.subject to 'courses_master'@'localhost';
grant select on library_db.library_books to 'courses_master'@'localhost';*/

