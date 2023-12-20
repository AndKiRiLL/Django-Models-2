from django.db import models

class User(models.Model):
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=35)
    login = models.CharField(max_length=35)

    def __str__(self):
        return self.name
