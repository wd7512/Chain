from django import forms

class init_form(forms.Form):
  username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }))
  ig_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }))
