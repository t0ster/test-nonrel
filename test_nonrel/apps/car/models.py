from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
