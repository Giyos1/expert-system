from django import forms
from django.core.exceptions import ValidationError


class StudentForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     p1 = self.cleaned_data["password1"]
    #     p2 = self.cleaned_data["password2"]
    #     if p1 != p2:
    #         raise ValidationError("bir xil emas")


class StudentEditForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()


class NewPasswordForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class ExportEmployeeForm(forms.Form):
    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=200, widget=forms.PasswordInput)

