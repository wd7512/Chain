from django.db import models
from django.forms import extras

# Create your models here.

class init_form(models.Model):

    sex_choices = [('M','Male'),('F','Female'),('O','Other')]
    
    username = models.CharField(max_length = 100)
    instagram_id = models.CharField(max_length = 100)
    sex = models.CharField(max_length = 1,choices = sex_choices,blank = True)
    submission_date = models.DateTimeField()
    birthdate = forms.DateField(widget=extras.SelectDateWidget)
