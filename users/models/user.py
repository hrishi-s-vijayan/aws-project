from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.name
