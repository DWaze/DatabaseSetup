from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base


class StateHistory(Base):
    __tablename__ = "statehistory"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    state = Column(String(250))

    # IOTNodes

    iotNodes_id = Column(Integer, ForeignKey('iotnode.id'))
