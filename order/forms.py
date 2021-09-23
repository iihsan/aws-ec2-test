from django import forms

class ContactUsForm(forms.Form):
  email = forms.EmailField(required=True)
  password = forms.CharField(widget=forms.PasswordInput(), required=True)