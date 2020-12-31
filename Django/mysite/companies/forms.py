from django import forms

BIRTH_YEAR_CHOICES = list(range(1900,2020-16))
SEX_CHOICES = [('M','Male'),('F','Female'),('O','Other')]


class init_form(forms.Form):
  username = forms.CharField()
  company_name = forms.CharField()


