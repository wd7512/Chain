from django import forms

BIRTH_YEAR_CHOICES = list(range(1900,2020-16))
SEX_CHOICES = [('M','Male'),('F','Female'),('O','Other')]


class init_form(forms.Form):
  # email = forms.CharField()
  company_name = forms.CharField()
  company_size = forms.IntegerField()
  company_business_area = forms.CharField()
  company_instagram_id = forms.CharField()




