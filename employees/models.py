from django.db import models

class Employee(models.Model):
    name = models.TextField(default='')
    email = models.TextField(default='')
    salary = models.DecimalField(decimal_places=0, max_digits=6)
    hired = models.DateField()
