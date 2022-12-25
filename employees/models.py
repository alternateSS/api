from django.db import models


class ManagePlacement(models.Model):
    position = models.CharField(max_length=40)
    department = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.position} - {self.department}'


class Employee(models.Model):
    fullname = models.CharField(max_length=35)
    date_birth = models.DateField()
    position = models.ForeignKey(ManagePlacement, on_delete=models.CASCADE)
    salary = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.fullname} - {self.position} - {self.salary}'