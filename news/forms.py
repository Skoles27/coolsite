from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class ContactForm(forms.ModelForm):
    captcha = CaptchaField(label="")

    class Meta:
        model = Contact
        fields = ("name", "surname", "email", "content", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-label mb-3", }),
            "surname": forms.TextInput(attrs={"class": "form-control mb-3", }),
            "email": forms.TextInput(attrs={"class": "form-control mb-3", "type": "email"}),
            "content": forms.Textarea(attrs={"class": "form-control mb-3"}),
        }
