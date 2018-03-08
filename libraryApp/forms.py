from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """docstring for SignUpForm"""
        def __init__(self, arg):
            super(SignUpForm, self).__init__()
            self.arg = arg
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        )
def save(self,commit=true):
    user = super(SignUpForm,self).save(commit=False)
    if commit
        user.save()
    return user

#refrences https://www.youtube.com/watch?v=66l9b2QrBR8
#refrences https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
