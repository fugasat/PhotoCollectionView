import datetime

from django.db import models
from django.utils import timezone


class Photo(models.Model):
    uid = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    favorites = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    regression_error = models.FloatField(default=0)
    features = models.TextField(default="")
    file_path = models.TextField(default="")

    def __str__(self):
        return str(self.pk) + ":" + str(self.uid) + ", " + str(self.date)

    def score(self):
        return int(self.regression_error)

    def date_label(self):
        return self.date.strftime("%Y/%m/%d")
