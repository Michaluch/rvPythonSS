SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `category_ibfk_1` FOREIGN KEY (`id`) REFERENCES `library_db`.`category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `comments`
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `creation_date` datetime NOT NULL,
  `title` varchar(128) NOT NULL,
  `body` text NOT NULL,
  `parent_type` int(2) unsigned NOT NULL,
  `parent_id` int(11) unsigned NOT NULL,
  `status` tinyint(2) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user` (`user_id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `course_subscriptions`
-- ----------------------------
DROP TABLE IF EXISTS `course_subscriptions`;
CREATE TABLE `course_subscriptions` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `course_id` int(11) unsigned NOT NULL,
  `status` tinyint(2) unsigned NOT NULL,
  `subscription_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user` (`user_id`),
  KEY `fk_course` (`course_id`),
  CONSTRAINT `course_subscriptions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `course_subscriptions_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `courses`
-- ----------------------------
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) unsigned NOT NULL,
  `author_id` int(11) unsigned NOT NULL,
  `difficulty_id` int(11) unsigned NOT NULL,
  `entity_type_id` int(11) unsigned NOT NULL,
  `name` varchar(128) NOT NULL,
  `description` text NOT NULL,
  `status` tinyint(1) unsigned NOT NULL,
  `has_test` tinyint(1) unsigned NOT NULL,
  `test_id` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_subject` (`subject_id`),
  KEY `fk_author` (`author_id`),
  KEY `fk_difficulty` (`difficulty_id`),
  KEY `fk_entity_type` (`entity_type_id`),
  CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `courses_ibfk_2` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `courses_ibfk_3` FOREIGN KEY (`difficulty_id`) REFERENCES `courses_difficulty` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `courses_ibfk_4` FOREIGN KEY (`entity_type_id`) REFERENCES `entity_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `courses_difficulty`
-- ----------------------------
DROP TABLE IF EXISTS `courses_difficulty`;
CREATE TABLE `courses_difficulty` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `entity_type`
-- ----------------------------
DROP TABLE IF EXISTS `entity_type`;
CREATE TABLE `entity_type` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `grade_details`
-- ----------------------------
DROP TABLE IF EXISTS `grade_details`;
CREATE TABLE `grade_details` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `grade_id` int(11) unsigned NOT NULL,
  `question_id` int(11) unsigned NOT NULL,
  `question_result` tinyint(2) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_grades` (`grade_id`),
  KEY `fk_question` (`question_id`),
  CONSTRAINT `grade_details_ibfk_1` FOREIGN KEY (`grade_id`) REFERENCES `grades` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `grade_details_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `test_questions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `grades`
-- ----------------------------
DROP TABLE IF EXISTS `grades`;
CREATE TABLE `grades` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `subscription_id` int(10) unsigned NOT NULL,
  `test_id` int(10) unsigned NOT NULL,
  `test_score` smallint(5) unsigned NOT NULL,
  `attempt` tinyint(3) unsigned NOT NULL,
  `date` datetime NOT NULL,
  `is_hidden` tinyint(1) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_subscription` (`subscription_id`),
  KEY `fk_test` (`test_id`),
  CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`subscription_id`) REFERENCES `course_subscriptions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `grades_ibfk_2` FOREIGN KEY (`test_id`) REFERENCES `tests` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `lecture_books`
-- ----------------------------
DROP TABLE IF EXISTS `lecture_books`;
CREATE TABLE `lecture_books` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `lecture_id` int(10) unsigned NOT NULL,
  `book_id` int(10) unsigned NOT NULL,
  `book_details` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_lecture` (`lecture_id`),
  KEY `fk_book` (`book_id`),
  CONSTRAINT `lecture_books_ibfk_1` FOREIGN KEY (`lecture_id`) REFERENCES `lectures` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `lecture_books_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `library_db`.`library_books` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `lectures`
-- ----------------------------
DROP TABLE IF EXISTS `lectures`;
CREATE TABLE `lectures` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `course_id` int(10) unsigned NOT NULL,
  `entity_type_id` int(10) unsigned NOT NULL,
  `title` varchar(200) NOT NULL,
  `body` text NOT NULL,
  `status` tinyint(2) unsigned NOT NULL,
  `has_test` tinyint(1) unsigned NOT NULL,
  `test_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_course` (`course_id`),
  KEY `fk_entity_type` (`entity_type_id`),
  CONSTRAINT `lectures_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `lectures_ibfk_2` FOREIGN KEY (`entity_type_id`) REFERENCES `entity_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `rating`
-- ----------------------------
DROP TABLE IF EXISTS `rating`;
CREATE TABLE `rating` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `entity_type_id` int(10) unsigned NOT NULL,
  `entity_id` int(10) unsigned NOT NULL,
  `course_average_rating` smallint(5) unsigned NOT NULL,
  `votes_count` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_entity_type` (`entity_type_id`),
  CONSTRAINT `rating_ibfk_1` FOREIGN KEY (`entity_type_id`) REFERENCES `entity_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `rating_details`
-- ----------------------------
DROP TABLE IF EXISTS `rating_details`;
CREATE TABLE `rating_details` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `rating_id` int(10) unsigned NOT NULL,
  `details` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user` (`user_id`),
  KEY `fk_rating` (`rating_id`),
  CONSTRAINT `rating_details_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `rating_details_ibfk_2` FOREIGN KEY (`rating_id`) REFERENCES `rating` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `roles`
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `subject`
-- ----------------------------
DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `category_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_category` (`category_id`),
  CONSTRAINT `subject_ibfk_1` FOREIGN KEY (`id`) REFERENCES `library_db`.`subject` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `subject_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `test_answers`
-- ----------------------------
DROP TABLE IF EXISTS `test_answers`;
CREATE TABLE `test_answers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `question_id` int(10) unsigned NOT NULL,
  `answer` varchar(300) NOT NULL,
  `is_correct` tinyint(1) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_question` (`question_id`),
  CONSTRAINT `test_answers_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `test_questions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `test_questions`
-- ----------------------------
DROP TABLE IF EXISTS `test_questions`;
CREATE TABLE `test_questions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `test_id` int(10) unsigned NOT NULL,
  `book_id` int(10) unsigned NOT NULL,
  `question_text` varchar(300) NOT NULL,
  `book_details` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_test` (`test_id`),
  KEY `fk_book` (`book_id`),
  CONSTRAINT `test_questions_ibfk_1` FOREIGN KEY (`test_id`) REFERENCES `tests` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `test_questions_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `library_db`.`library_books` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tests`
-- ----------------------------
DROP TABLE IF EXISTS `tests`;
CREATE TABLE `tests` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `entity_type_id` int(10) unsigned NOT NULL,
  `name` varchar(120) NOT NULL,
  `description` varchar(400) NOT NULL,
  `questions_amount` tinyint(3) unsigned NOT NULL,
  `status` tinyint(2) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_entity_type` (`entity_type_id`),
  CONSTRAINT `tests_ibfk_1` FOREIGN KEY (`entity_type_id`) REFERENCES `entity_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `role_id` int(10) unsigned NOT NULL,
  `f_name` varchar(50),
  `l_name` varchar(50),
  `login` varchar(20) NOT NULL,
  `password` char(41) NOT NULL,
  `pass_salt` char(20) DEFAULT NULL,
  `email` varchar(20),
  `status` tinyint(4),
  `reg_date` datetime,
  PRIMARY KEY (`id`),
  KEY `fk_role` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
