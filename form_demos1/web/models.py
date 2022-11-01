from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    pets = models.ManyToManyField(Pet, )
