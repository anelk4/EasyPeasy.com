from .models import Tutors
from .models import Playlist
from .models import Likes
from .models import Content
from .models import Bookmark
from .models import Comments
from django.forms import ModelForm,TextInput,ClearableFileInput,DateField,CharField,PasswordInput
from django.core.exceptions import ValidationError

from django.forms import ModelForm #TextInput,ClearableFileInput,DateField,CharField,PasswordInput
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import authenticate
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




class DeleteCommentForm(forms.Form):
    delete_comment = forms.BooleanField(
        widget=forms.HiddenInput(attrs={
            'class': 'form-control',
        }),
        initial=True,
        required=False,
    )







class SavePlaylistForm(forms.Form):
    save_playlist = forms.BooleanField(required=False, widget=forms.HiddenInput())

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['save_playlist'].label = ''
        self.fields['save_playlist'].widget.attrs.update({'class': 'save-playlist-btn'})







class CourseRequestForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    age = forms.IntegerField(min_value=18, max_value=99)
    weight = forms.DecimalField(max_digits=5, decimal_places=2)
    is_accepted = forms.BooleanField(required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time_of_birth = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    website = forms.URLField()
    resume = forms.FileField()
    profile_picture = forms.ImageField()








class TutorsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Tutors
        fields = ['name', 'profession', 'email', 'password', 'password2', 'image']






class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['fk_tutor_id', 'title', 'description', 'thumb', 'status']








class LikesForm(forms.ModelForm):
    LIKE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    like_status = forms.ChoiceField(choices=LIKE_CHOICES)









    class Meta:
        model = Likes
        fields = ['fk_pklikes_user_id', 'fk_tutor_idlikes', 'fk_content_idlikes', 'like_status']








    class ContentForm(forms.ModelForm):
        class Meta:
            model = Content
            fields = ['fk_tutor_idcontent', 'fk_playlist_id', 'titlecontent', 'description_content', 'video', 'thumb',
                      'status']

        # Add additional form fields here
        additional_field_1 = forms.CharField(max_length=50, required=False)
        additional_field_2 = forms.BooleanField(required=False)

    class BookmarkForm(forms.ModelForm):
        class Meta:
            model = Bookmark
            fields = ['fk_user_id', 'fk_playlist_id']

        def clean(self):
            cleaned_data = super().clean()
            user_id = cleaned_data.get('fk_user_id')
            playlist_id = cleaned_data.get('fk_playlist_id')
            if Bookmark.objects.filter(fk_user_id=user_id, fk_playlist_id=playlist_id).exists():
                raise forms.ValidationError('Bookmark already exists for this user and playlist.')
            return cleaned_data

    class CommentsForm(forms.ModelForm):
        name = forms.CharField(max_length=50, label='Your name', required=True)
        email = forms.EmailField(max_length=100, label='Your email', required=True)

        class Meta:
            model = Comments
            fields = ['fk_content_id', 'fk_user_id', 'fk_tutor_id', 'comment']
            widgets = {
                'fk_content_id': forms.HiddenInput(),
                'fk_user_id': forms.HiddenInput(),
                'fk_tutor_id': forms.HiddenInput(),
            }

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            if not name:
                raise forms.ValidationError('Please enter your name.')
            if not email:
                raise forms.ValidationError('Please enter your email.')
            return cleaned_data




class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'box',
        'placeholder': 'Введите email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'box',
        'placeholder': 'Введите пароль'
    }))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Неправильный email или пароль')