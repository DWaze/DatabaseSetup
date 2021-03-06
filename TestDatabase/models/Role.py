from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base


association_table2 = Table('rNodes', Base.metadata,
                           Column('role_id', Integer, ForeignKey('role.id')),
                           Column('iotNode_id', Integer, ForeignKey('iotnode.id')),
                           )

class Constraint(Base):
    __tablename__= 'constraint'
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    account = relationship("Account", back_populates="constraints")
    role = relationship("Role", back_populates="constraints")

    def __init__(self,startDate,endDate):
        self.startDate = startDate
        self.endDate = endDate

    def addRole(self, role):
        if self not in role.accounts:
            if self.role is not None:
                self.role.removeAccount(self)
            self.role = role

    def addAccount(self, account):
        if self not in account.roles:
            if(self.account is not None):
                self.account.removeRole(self)
            self.account = account



class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

    # IOTNodes

    def __init__(self, name):
        self.name = name

    iotNodes = relationship("IoTNode", secondary=association_table2)

    def addIoTNode(self,iotNode):
        if iotNode not in self.iotNodes :
            self.iotNodes.append(iotNode)

    # Accounts

    constraints = relationship("Constraint",
                            back_populates="role")

    def removeConstraint(self, account):
        self.constraints.remove(account)

    def addConstraint(self, constraint):
        if constraint not in self.constraints:
            if constraint.role is not None:
                constraint.role.removeConstraint(constraint)
            constraint.role=self

