from sqlalchemy import (
    UnicodeText,
    Column,
    Integer,
    Unicode,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

from pyramid.security import Authenticated
from pyramid.security import Allow
from pyramid.security import Deny


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(Unicode)
    password = Column(Unicode)
    role_id = Column(Integer)

    def __init__(self, login, password, role_id):
        self.login = login
        self.password = password
        self.role_id = role_id


class Courses(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer)
    author_id = Column(Integer)
    difficulty_id = Column(Integer)
    entity_type_id = Column(Integer)
    name = Column(Unicode)
    description = Column(UnicodeText)
    status = Column(Integer)
    has_test = Column(Integer)
    test_id = Column(Integer)

    def __init__(self,
                 subject_id,
                 author_id,
                 difficulty_id,
                 entity_type_id,
                 name,
                 description,
                 status,
                 has_test,
                 test_id):
        self.subject_id = subject_id
        self.author_id = author_id
        self.difficulty_id = difficulty_id
        self.entity_type_id = entity_type_id
        self.name = name
        self.description = description
        self.status = status
        self.has_test = has_test
        self.test_id = test_id


class RootFactory(object):
    __acl__ = [
        (Deny, 'mike', 'view'),
        (Allow, Authenticated, 'view')
    ]

    def __init__(self, request):
        pass


def check_login(login, password):
    session = DBSession()
    user = session.query(Users).filter_by(login=login).first()
    if user is not None:
        if user.password == password:
            return True
    return False


def get_courses():
    session = DBSession()
    courses = session.query(Courses.name, Courses.description).all()
    return courses
