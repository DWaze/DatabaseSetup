from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base


class Pins(Base):
    __tablename__ = "pins"
    id = Column(Integer, primary_key=True)
    nodePin = Column(String(250))
    gpioPin = Column(String(250))

    # IoTNodes

    iotNode_id = Column(Integer, ForeignKey('iotnode.id'))
    iotNode = relationship("IoTNode", back_populates="pins")

    def addIoTNode(self, iotNode):
        if self not in iotNode.pins:
            if self.iotNode is not None:
                iotNode.removePin(self)
            self.iotNode = iotNode