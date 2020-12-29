from django.db import models

# Create your models here.

class user_form(models.Model):

    sex_choices = [('M','Male'),('F','Female'),('O','Other')]
    
    username = models.CharField(max_length = 100)
    instagram_id = models.CharField(max_length = 100)
    sex = models.CharField(max_length = 1,choices = sex_choices,blank = True)
    submission_date = models.DateTimeField(default=None)
    birthday = models.DateTimeField(default=None)
