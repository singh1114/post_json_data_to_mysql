from __future__ import unicode_literals

from django.db import models

# Create your models here.
class newmodel(models.Model):
    wholestring = models.CharField(max_length = 10000)
