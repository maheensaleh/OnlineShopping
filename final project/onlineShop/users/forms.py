from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

'''this file handles the customer sign up form'''

'''the following three exception classes are to handle the validation errors
due to invalid entries in the user creation form'''


class PasswordLength(Exception):
    value = False
    message = 'Your password must have atleast 8 characters'


class InvalidUsername(Exception):
    value = False
    message = 'Your username is not acceptable'


class PasswordMismatch(Exception):
    value = False
    message = '''Your password is either too short or invalid or it doesn't match with the second password'''


class InvalidEmail(Exception):
    value = False
    message = 'Your email id is not acceptable'


class CustomerForm(UserCreationForm): # usercreation form is built-in
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']   #for additional fields

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)

        try:
            if r.count():  # checks whether the entered user name already exists or not
                raise InvalidUsername

        except InvalidUsername:
            InvalidUsername.value = True

        else:
            return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)

        try:
            if r.count():
                raise InvalidEmail

        except InvalidEmail:
            InvalidEmail.value = True

        else:
            return email

    def clean_password2(self):      #confirm password
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print(password1,password2)
        try:
            if password1 and password2 and password1 != password2:
                raise PasswordMismatch

            if len(password1)<8:
                raise PasswordLength

        except PasswordMismatch:
            PasswordMismatch.value = True

        except PasswordLength:
            PasswordLength.value = True

        else:
            return password2