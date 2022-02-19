from django import forms
from .models import user
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
    class Meta:
        model = user
        fields = ('fname', 'lname', 'email', 'phone', 'password', 'confirm_password', 'image')

    def clean(self):
        # return dict containing cleaned data
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
    #
    def clean_email(self):
            email = self.cleaned_data['email']
            if user.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists")
            return email

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        e_user = user.objects.filter(email=email,password=password)
        if len(e_user) > 0:
            e_user = e_user[0]
        if not e_user:
            raise forms.ValidationError('invalid login data!')

class DateInput(forms.DateInput):
    input_type = 'date'

class UpdateProfile(forms.ModelForm):
    date_birth = forms.DateField(required=False, widget=DateInput())
    #photo = forms.ImageField(required=False, widget=forms.FileInput)
    facebook_link = forms.URLField(required=False)
    country = forms.CharField(required=False)

    class Meta:
        model = user
        fields = ('fname', 'lname', 'phone', 'date_birth', 'facebook_link', 'country', 'image')

    def clean_country(self):
        if self.is_valid():
            country = self.cleaned_data['country']
            if country:
                return country
            else:
                return None

    def clean_facebook_link(self):
        if self.is_valid():
            facebook_link = self.cleaned_data['facebook_link']
            if facebook_link:
                return facebook_link
            else:
                return None

    def clean_date_birth(self):
        if self.is_valid():
            date_birth = self.cleaned_data['date_birth']
            if date_birth:
                return date_birth
            else:
                return None




