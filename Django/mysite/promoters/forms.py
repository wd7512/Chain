from django import forms
from django.forms import ModelForm
from .models import Order


BIRTH_YEAR_CHOICES = list(range(1900, 2020 - 16))
SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]


class init_form(forms.Form):
    # username = forms.CharField()
    ig_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Instagram Username',
                                                            'class': 'form-control',
                                                            }))

    birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={
        "class": "test form-control"
    })
                               )
    sex = forms.MultipleChoiceField(choices=SEX_CHOICES)

    followers = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Follower Number',
                                                                   'class': 'form-control',
                                                                   }))



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'