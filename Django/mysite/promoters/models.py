from django.db import models

# Create your models here.

class user_form(models.Model):

    sex_choices = [('M','Male'),('F','Female'),('O','Other')]
    email = models.CharField(max_length = 100,default=None)
    instagram_id = models.CharField(max_length = 100,default=None)
    sex = models.CharField(max_length = 1,choices = sex_choices,blank = True,default=None)
    submission_date = models.DateTimeField(default=None)
    birthday = models.DateTimeField(default=None)
    followers = models.IntegerField(default=None)

    def __str__(self):
        return self.email
        return self.instagram_id
        return self.sex
        return self.birthday #need this to display data when Quering db
        return self.followers