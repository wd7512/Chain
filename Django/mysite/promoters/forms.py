from django import forms

BIRTH_YEAR_CHOICES = list(range(1900,2020-16))
SEX_CHOICES = [('M','Male'),('F','Female'),('O','Other')]


class init_form(forms.Form):
  username = forms.CharField()
  ig_name = forms.CharField()
  birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
  sex = forms.MultipleChoiceField(choices = SEX_CHOICES)
  followers = forms.IntegerField()
