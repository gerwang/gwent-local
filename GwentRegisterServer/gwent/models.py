# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Player(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    rating = models.IntegerField(default=1000)

    def __str__(self):
        return self.username + ': ' + str(self.rating)
