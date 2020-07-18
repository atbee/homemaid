from django.db import models


class Maid(models.Model):
    name = models.CharField(max_length=300)
    birthdate = models.DateField()
    description = models.TextField()
    certificate = models.TextField()
    salary = models.IntegerField()
