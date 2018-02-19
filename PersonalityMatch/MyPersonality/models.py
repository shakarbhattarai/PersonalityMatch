# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PersonalityDetails(models.Model):
    userName=models.CharField(max_length=50)
    question=models.CharField(max_length=3)
    answer=models.IntegerField(max_length=2)


    def __str__(self):
        return self.userName