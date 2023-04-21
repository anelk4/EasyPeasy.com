from .models import Users
from .models import Tutors
from .models import Playlist
from .models import Likes
from .models import Content
from .models import Bookmark
from .models import Comments
from django.forms import ModelForm

class UsersForm(ModelForm):
    class Meta:
        model=Users
        fields= ['pkid','name','email','password','image']
