from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base


class Action(Base):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))

    # NodeType

    nTypeId = Column(Integer, ForeignKey('nodetype.id'))
    nodetype = relationship("NodeType", back_populates="actions")

    def addNType(self, nodetype):
        if self not in nodetype.actions:
            if self.nodetype is not None:
                nodetype.removeAction(self)
            self.nodetype = nodetype

    # ActionHistory

    actionHistories = relationship("ActionHistory", back_populates="action")

    def removeActionH(self, actionHistorie):
        self.actionHistories.remove(actionHistorie)

    def addActionH(self, actionHistorie):
        if actionHistorie not in self.actionHistories:
            if actionHistorie.action is not None:
                actionHistorie.action.removeActionH(actionHistorie)

            self.actionHistories.append(actionHistorie)
