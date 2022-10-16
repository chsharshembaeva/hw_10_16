from django.db import models


class Position(models.Model):
    position_name = models.CharField(max_length=40)
    department = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.position_name} - {self.department}'


class Employee(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    salary = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.position}'
