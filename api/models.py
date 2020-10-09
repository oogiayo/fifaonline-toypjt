from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    accessId = models.CharField(primary_key=True, max_length=24)
    nickname = models.CharField(max_length=128)
    level = models.IntegerField()
