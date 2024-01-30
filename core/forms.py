from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter Email"}
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Username"}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        )
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter First Name"}
        ),
        required=False,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    profile_pic = forms.ImageField(
        widget=forms.FileInput(
            attrs={"class": "form-control", "placeholder": "Upload image"}
        ),
        required=False,
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"}), required=False
    )

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "profile_pic",
            "address",
            "phone",
            "role",
            "bio",
        ]
