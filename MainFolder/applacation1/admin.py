from django.contrib import admin
from .models import Users
from .models import Tutors
from .models import Playlist
from .models import Likes
from .models import Content
from .models import Bookmark
from .models import Comments

admin.site.register(Users)
admin.site.register(Tutors)
admin.site.register(Playlist)
admin.site.register(Likes)
admin.site.register(Content)
admin.site.register(Bookmark)
admin.site.register(Comments)


