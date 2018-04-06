from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Toppings(models.Model):
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Toppings)


class Person(models.Model):
    name = models.CharField(max_length=50, default='none')


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person,
                                     through='Membership',
                                     through_fields=('group', 'person'),
                                     )


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE,default='', null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE,default='', null=False)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

    # class Meta:
    #     unique_together = (('group', 'person'),)


class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervisor_of',
    )
