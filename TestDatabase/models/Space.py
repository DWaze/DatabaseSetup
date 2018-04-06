from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base


class Space(Base):
    __tablename__ = "space"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    surface = Column(Float)
    spaceType = Column(String(250))
    floorNBR = Column(Integer)

    # Agent

    agentID = Column(Integer, ForeignKey('agent.id'))
    agent = relationship("Agent", back_populates="spaces")

    # Objects

    objects = relationship("Object")

    def addAgent(self, agent):
        if self not in agent.spaces:
            if self.agent is not None:
                agent.removeSpace(self)
            self.agent = agent


    def addObject(self,object):
        if object not in self.objects :
            self.objects.append(object)