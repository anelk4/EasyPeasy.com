from django import forms
from .models import Users
from .models import Tutors
from .models import Playlist
from .models import Likes
from .models import Content
from .models import Bookmark
from .models import Comments
from django.forms import ModelForm,TextInput,ClearableFileInput,DateField,CharField

class UsersForm(ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'box',
        'placeholder': 'Подтвердить пароль'
    }))
    class Meta:

        model=Users
        fields= ['name','email','password','password2','image']
        widgets={
            "name":TextInput(attrs={
                'class':'box',
                'placeholder':'Пример: Акжан'
            }),
            "email": TextInput(attrs={
                'class': 'box',
                'placeholder': 'Пример: Akzhan@gmail.com'
            }),
            "password": TextInput(attrs={
                'class': 'box',
                'placeholder': 'Поля для пароля'
            }),
            "image": ClearableFileInput(attrs={
                'class': 'box',
            })

        }
