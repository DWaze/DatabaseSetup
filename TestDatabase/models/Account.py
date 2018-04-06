from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base
from TestDatabase.models.Role import Constraint


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    userName = Column(String(250))
    password = Column(String(250))
    email = Column(String(250))
    type = Column(String(250))
    token = Column(String(250))
    tokenIssueDate = Column(DateTime)
    enabled = Column(Boolean)
    lastLogin = Column(DateTime)
    firstAccess = Column(DateTime)
    lastAccess = Column(DateTime)

    def __init__(self, userName, password, email):
        self.userName = userName
        self.password = password
        self.email = email

    # Role

    constraints = relationship("Constraint",
                        back_populates="account")

    def removeConstraint(self, constraint):
        self.constraints.remove(constraint)

    def addConstraint(self, constraint):
        if constraint not in self.constraints:
            if constraint.account is not None:
                constraint.account.removeConstraint(constraint)
            constraint.account = self

    # User

    user = relationship("User", uselist=False, back_populates="account")

    def addUser(self, user):
        if user.account is not None:
            user.account = None

        if self.user is not None:
            self.user.account = None

        self.user = user
