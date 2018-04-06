import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#  One to Many bid

# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250))
#     children = relationship("Child")
#
#
# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))
#     parent = relationship("Parent", back_populates = "children")


# Many to Many

association_table = Table('association', Base.metadata,
                          Column('parent_id', Integer, ForeignKey('parent.id'),nullable=False),
                          Column('child_id', Integer, ForeignKey('child.id'),nullable=False),
                          Column('date', Integer)
                          )


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    children = relationship("Child",
                            secondary=association_table,
                            back_populates="parents")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    parents = relationship("Parent",
                           secondary=association_table,
                           back_populates="children")


engine = create_engine('sqlite:///sqlalchemy_example1.db')

Base.metadata.create_all(engine)
