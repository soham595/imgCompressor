#Import base user class that we have on admin
from django.contrib.auth.models import User
from django import forms

#Creating blueprint for login form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    # Meta class has information about class
    class Meta:
        # When user signs up, they are added to the user class that we have on admin
        model = User
        #Fields that we want to appear are listed
        fields = ['username', 'email', 'password']