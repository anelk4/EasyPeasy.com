from .models import Tutors
from .models import Playlist
from .models import Likes
from .models import Content
from .models import Bookmark
from .models import Comments
from django.forms import ModelForm,TextInput,ClearableFileInput,DateField,CharField,PasswordInput
from django.core.exceptions import ValidationError

from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import TextInput, PasswordInput, ClearableFileInput
from .models import Users

class UsersForm(ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'box',
        'placeholder': 'Подтвердить пароль'
    }))

    class Meta:
        model = Users
        fields = ['name', 'email', 'password', 'password2', 'image']
        widgets = {
            "name": TextInput(attrs={
                'class': 'box',
                'placeholder': 'Пример: Акжан'
            }),
            "email": TextInput(attrs={
                'class': 'box',
                'placeholder': 'Пример: Akzhan@gmail.com'
            }),
            "password": PasswordInput(attrs={
                'class': 'box',
                'placeholder': 'Поля для пароля'
            }),
            "image": ClearableFileInput(attrs={
                'class': 'box',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )



