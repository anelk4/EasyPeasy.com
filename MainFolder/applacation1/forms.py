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



class UpdateProfileForm(forms.Form):
    name = forms.CharField(max_length=50, required=True) # name field
    email = forms.EmailField(required=True) # email field
    old_password = forms.CharField(widget=forms.PasswordInput, max_length=20, required=True) # previous password field
    new_password = forms.CharField(widget=forms.PasswordInput, max_length=20, required=True) # new password field
    confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=20, required=True) # confirm new password field
    profile_picture = forms.ImageField(required=False) # profile picture field



    # Method to clean and validate the new password fields
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError("New passwords must match.")







class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    number = forms.IntegerField(required=True)
    msg = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'cols': 30, 'rows': 10}), required=True)




class TeacherRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())



class GenderForm(forms.Form):
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])



class FoodForm(forms.Form):
    food_choices = [('1', 'Pizza'), ('2', 'Burger'), ('3', 'Tacos'), ('4', 'Sushi')]
    favourite_food = forms.MultipleChoiceField(choices=food_choices)





class AddCommentForm(forms.Form):
    comment_box = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите свой комментарий',
            'maxlength': 1000,
            'cols': 30,
            'rows': 10,
            'required': True,
            'class': 'form-control',
        }),
    )


