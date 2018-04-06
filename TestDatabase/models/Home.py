from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base


class Home(Base):
    __tablename__ = "home"
    id = Column(Integer, primary_key=True)
    address = Column(String(100))
    floor = Column(Integer)
    typeHome = Column(String(250))
    country = Column(String(250))
    city = Column(String(250))
    longitude = Column(Float)
    latitude = Column(Float)

    def __init__(self, address="", floor=0, typeHome="", country="", city="", longitude=0.0, latitude=0.0):
        self.address = address
        self.floor = floor
        self.typeHome = typeHome
        self.country = country
        self.city = city
        self.longitude = longitude
        self.latitude = latitude



    # Agents

    agents = relationship("Agent", back_populates="home")
    agentSup = relationship("Agent", uselist=False, back_populates="home")

    def removeAgent(self, agent):
        self.agents.remove(agent)

    def addAgent(self, agent):
        if agent not in self.agents:
            if agent.home is not None:
                agent.home.removeAgent(agent)

            self.agents.append(agent)

    def addAgentSup(self, agentSup):
        if agentSup.home is not None:
            agentSup.home = None

        if self.agentSup is not None:
            self.agentSup.home = None

        self.agentSup = agentSup
        agentSup.home = self

