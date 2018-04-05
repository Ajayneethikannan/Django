from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(label='username' ,max_length=30 )
    password = forms.PasswordInput()
