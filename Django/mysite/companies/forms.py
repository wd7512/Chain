from django import forms

BIRTH_YEAR_CHOICES = list(range(1900,2020-16))
SEX_CHOICES = [('M','Male'),('F','Female'),('O','Other')]


class init_form(forms.Form):
  company_name = forms.CharField(
                                 max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': 'Company Name',
                                                               'class': 'form-control',
                                                               }))
  company_size = forms.IntegerField(
                                    widget=forms.NumberInput(attrs={'placeholder': 'Number of Employees',
                                                                    'class': 'form-control'}))
  company_business_area = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Business Area',
                                                                        'class': 'form-control'}))
  company_instagram_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Instagram Id',
                                                                       'class': 'form-control'}))




