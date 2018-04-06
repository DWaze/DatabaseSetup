from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from TestDatabase.models.base import Base


class Object(Base):
    __tablename__ = "object"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    longitude = Column(Float)
    latitude = Column(Float)

    # IOT_Nodes

    ioT_Nodes = relationship("IoTNode", back_populates="object")

    # Spaces ID

    spaces_id = Column(Integer, ForeignKey('space.id'))

    def removeIoTNode(self, iotNode):
        self.ioT_Nodes.remove(iotNode)

    def addIoTNode(self, iotNode):
        if iotNode not in self.ioT_Nodes:
            if iotNode.object is not None:
                iotNode.object.removeIoTNode(iotNode)

            self.ioT_Nodes.append(iotNode)
