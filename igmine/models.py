from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class image(models.Model):
    title = models.CharField(max_length=255)

    user_id = models.IntegerField()
    pub_date = models.DateTimeField('date_pubished')