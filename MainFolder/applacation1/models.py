from django.db import models
from django.contrib.auth.hashers import make_password
class Users(models.Model):
    pkid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Users, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pkid)



class Tutors(models.Model):
    pkidtutors = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    image = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pkidtutors)



class Playlist(models.Model):
    pkidplaylist = models.AutoField(primary_key=True)
    fk_tutor_id = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    thumb = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='deactive')

    def __str__(self):
        return str(self.pkidplaylist)




class Likes(models.Model):
    fk_pklikes_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    fk_tutor_idlikes = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    fk_content_idlikes = models.ForeignKey('Content', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fk_pklikes_user_id)




class Content(models.Model):
    pkid_content = models.AutoField(primary_key=True)
    fk_tutor_idcontent = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    fk_playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    titlecontent = models.CharField(max_length=100)
    description_content = models.CharField(max_length=1000)
    video = models.CharField(max_length=100)
    thumb = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='deactive')

    def __str__(self):
        return str(self.pkid_content)




class Bookmark(models.Model):
    fk_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    fk_playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fk_user_id)




class Comments(models.Model):
    pkid_comments = models.AutoField(primary_key=True)
    fk_content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    fk_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    fk_tutor_id = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.pkid_comments)



