from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)

    def __repr__(self):
        return "<Dojo object: {} {}>".format(self.name, self.desc)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # One dojo can have many Ninja's attending.
    dojo = models.ForeignKey(Dojo, related_name="ninjas")

    def __repr__(self):
        return "<Ninja object: {} {}>".format(self.name, self.desc)
