from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """docstring for SignUpForm"""
        def __init__(self, arg):
            super(SignUpForm, self).__init__()
            self.arg = arg
    users_fname = forms.CharField(max_length=30, required=False, help_text='Optional.')
    users_lname = forms.CharField(max_length=30, required=False, help_text='Optional.')
    user_email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
        'users_uname',
        'users_fname',
        'users_lname',
        'user_email',
        'users_password',
        'users_password2'
        )
def save(self,commit=true):
    user = super(SignUpForm,self).save(commit=False)
    if commit
        user.save()
    return user

#refrences https://www.youtube.com/watch?v=66l9b2QrBR8
#refrences https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
