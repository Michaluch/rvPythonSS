from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
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
