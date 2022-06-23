from django.db import models
from django.contrib.auth.models import User
import datetime


class Sheet(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateField(default=datetime.date.today)
    # TODO: Add this to storage object
    # TODO: Unhardcode this
    sheet = models.FileField(upload_to='uploads/sheets')
    author = models.CharField(max_length=256)
    publisher = models.ForeignKey(User, related_name='sheets', on_delete=models.CASCADE)
