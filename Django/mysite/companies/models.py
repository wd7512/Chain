from django.db import models

# Create your models here.

class company_form(models.Model):

    email = models.CharField(max_length = 100,default=None)
    company_name = models.CharField(max_length = 100,default=None)
    submission_date = models.DateTimeField(default=None)
    company_size = models.IntegerField(default=None)
    company_business_area = models.CharField(max_length = 100,default=None)
    company_instagram_id = models.CharField(max_length = 100,default=None)
    verified = models.IntegerField(default=0)

    def __str__(self):
        return self.email
        return self.company_name
        return self.submission_date
        return self.company_size #need this to display data when Quering db
        return self.company_business_area
        return self.instagram_id
        return self.verified
