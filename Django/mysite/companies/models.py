from django.db import models

# Create your models here.

class company_form(models.Model):

    username = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)
    submission_date = models.DateTimeField(default=None)
    verified = models.IntegerField(default=0)
