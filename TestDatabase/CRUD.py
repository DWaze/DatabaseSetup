from TestDatabase.models import Person, Group, Membership

p1 = Person(name='Mohamed')
p2 = Person(name='Redha')
p3 = Person(name='Sami')
p4 = Person(name='Hamouda')
g1 = Group(name='Mega Structure')
g2 = Group(name='Intersection Resumer')
g3 = Group(name='Mal Functioning')
g4 = Group(name='Super Hypers')
p1.save()
p2.save()
p3.save()
p4.save()
g1.save()
g2.save()
g3.save()
g4.save()
members_1 = Membership(invite_reason='Job Work')
members_2 = Membership(invite_reason='Job Work')
members_3 = Membership(invite_reason='Modeling Work')
members_1.group = g1

members_2.group = g1
members_3.group = g2
members_1.person = p1
members_2.person = p1
members_3.person = p2
members_1.inviter = p1
members_2.inviter = p1
members_3.inviter = p2
members_1.save()
members_2.save()
members_3.save()


# members_2 = Membership.objects.filter(id)

members_2= Group.objects.get(pk=3)
# members_2.person = Person.objects.get(pk=5)
# members_1.save()
