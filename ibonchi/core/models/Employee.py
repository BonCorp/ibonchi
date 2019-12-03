from django.db import models
from django.contrib.auth.models import User


# create Menu Item Model
class Employee(models.Model):
    Chef = 'Chef'
    Manager = 'Manager'
    Server = 'Server'
    Host = 'Host'
    Bartender = 'Bartender'

    employee_position_choices = [
        (Chef, 'Chef'),
        (Manager, 'Manager'),
        (Server, 'Server'),
        (Host, 'Host'),
        (Bartender, 'Bartender'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=64)
    position = models.CharField(choices=employee_position_choices, max_length=21, default=Server)
    photo = models.ImageField(upload_to='employees')

    def __str__(self):
        return f"{self.user}'s Employee: {self.name} - {self.position}"
