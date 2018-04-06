from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base


class Agent(Base):
    __tablename__ = "agent"
    id = Column(Integer, primary_key=True)
    ipAddress = Column(String(100))


    def __init__(self, ipAddress="169.254.255.254"):
        self.ipAddress = ipAddress


    # Home

    homeId = Column(Integer, ForeignKey("home.id"))
    home = relationship("Home", back_populates="agents")

    def addHomeSup(self, home):
        if home.agentSup is not None:
            home.agentSup = None

        if self.home is not None:
            self.home.agentSup = None

        self.home = home
        home.agentSup = self

    def addHome(self, home):
        if self not in home.agents:
            if self.home is not None:
                home.removeAgent(self)
            self.home = home


    # Spaces

    spaces = relationship("Space", back_populates="agent")

    def removeSpace(self, space):
        self.spaces.remove(space)

    def addSpace(self, space):
        if space not in self.spaces:
            if space.agent is not None:
                space.agent.removeSpace(space)

            self.spaces.append(space)
