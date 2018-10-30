from django.db import models

# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=20)

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    roles = models.ManyToManyField(Role, through='UsersRoles')

class UsersRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigneddate = models.DateField()
