from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    )

from sqlalchemy.dialects.mssql import (
    TINYINT,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class ModelUsers(Base):
    __tablename__ = 'users'
    id = Column(Integer(10), primary_key=True)
    role_id = Column(Integer(10))
    f_name = Column(String(50))
    l_name = Column(String(50))
    login = Column(String(20))
    password = Column(String(20))
    email = Column(String(20))
    status = Column(TINYINT(4))

    def __init__(self, role_id, f_name, l_name, login, password, email, status):
        self.role_id = role_id
        self.f_name = f_name
        self.l_name = l_name
        self.login = login
        self.password = password
        self.email = email
        self.status = status

#Index('my_index', MyModel.name, unique=True, mysql_length=255)
