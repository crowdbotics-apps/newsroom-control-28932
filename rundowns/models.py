from django.conf import settings
from django.db import models


class Rundown(models.Model):
    "Generated Model"
    name = models.TextField()
    segment = models.TextField()


# Create your models here.
