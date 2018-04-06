from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime
import TestDatabase.models.base
import TestDatabase.models.Account
import TestDatabase.models.Action
import TestDatabase.models.ActionHistory
import TestDatabase.models.Agent
import TestDatabase.models.Home
import TestDatabase.models.IoTNode
import TestDatabase.models.NodeType
import TestDatabase.models.Object
import TestDatabase.models.Pins
from TestDatabase.models.Role import Role
from TestDatabase.models.Role import Constraint
from TestDatabase.models.Account import Account
import TestDatabase.models.Space
import TestDatabase.models.StateHistory
import TestDatabase.models.User
from TestDatabase.models.Agent import Agent
from TestDatabase.models.Home import Home

engine = create_engine("sqlite:///iot.db")
TestDatabase.models.base.Base.metadata.create_all(engine, checkfirst=True)

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)

session = DBSession()

agent1 = Agent()
agent1.ipAddress = "192.168.1.123"
agent2 = Agent("192.168.1.124")
agent3 = Agent("192.168.1.125")
agent4 = Agent("192.168.1.126")
agent5 = Agent("192.168.1.127")

house1 = Home("Constantine 1000 log", 2, "A4", "Algeria", "Constantine", 32.256516, 25.2365165)
house2 = Home("Sétif 1000 log", 3, "A2", "Algeria", "Sétif", 32.256516, 25.2365165)
house3 = Home("El Elma 1000 log", 4, "A3", "Algeria", "El Elma", 32.256516, 25.2365165)
house4 = Home("Mssila 1000 log", 5, "A1", "Algeria", "Mssila", 32.256516, 25.2365165)
house5 = Home("Constantine 1023 log", 6, "A5", "Algeria", "Constantine", 32.256516, 25.2365165)

house1.addAgent(agent1)
house1.addAgent(agent2)

house2.addAgent(agent1)
house2.addAgent(agent3)

house3.addAgent(agent1)
house3.addAgent(agent5)

agent4.addHome(house4)

session.add_all([agent1, agent2, agent3, agent4, agent5, house1, house2, house3, house4, house5])
session.commit()

role1 = Role("admin")
role2 = Role("sub-admin")
role3 = Role("user")

account1 = Account("redha", "mohamed", "mail@mail.com")
account2 = Account("sami", "khammar", "mail@hotmail.com")
account3 = Account("mega", "pupi", "gmai@mailo.com")

constraint1 = Constraint(datetime.datetime.utcnow(), datetime.datetime.utcnow())
constraint2 = Constraint(datetime.datetime.utcnow(), datetime.datetime.utcnow())
constraint3 = Constraint(datetime.datetime.utcnow(), datetime.datetime.utcnow())


account1.addConstraint(constraint1)
role1.addConstraint(constraint1)
account1.addConstraint(constraint1)
role2.addConstraint(constraint2)
account1.addConstraint(constraint2)
role3.addConstraint(constraint3)
account1.addConstraint(constraint3)

account2.addConstraint(constraint1)


session.add_all([role1, role2, role3, account1, account2, account3, constraint1, constraint2, constraint3])
session.commit()


accounts = session.query(Account).all()

for account in accounts:
    print(account.userName)

