from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    holder = models.ForeignKey(User,
    related_name='holders', on_delete=models.CASCADE,
    null=True,
    )

    def __str__(self):
        return f"{self.name}: {self.holder}"


class Bank(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title