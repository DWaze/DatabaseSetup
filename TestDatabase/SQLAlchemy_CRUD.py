from TestDatabase.sqlalchemy_test import Base, Parent, Child
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqlalchemy_example1.db')
Base.metadata.bind = engine

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)

session = DBSession()

p1 = Parent(name='new person')
p2 = Parent(name='new person')
p3 = Parent(name='new person')
ch1 = Child()
ch2 = Child()
ch3 = Child()

p1.children.append(ch1)
p1.children.append(ch2)
p1.children.append(ch3)
p2.children.append(ch2)
p2.children.append(ch1)
p2.children.append(ch3)


session.add_all([p1, p2, ch1, ch2, ch3])
session.commit()

parent1=session.query(Parent).all()

i=0
for parent in parent1:
    print(parent.name)
    i=i+1

print(i)

child1=session.query(Child).all()










