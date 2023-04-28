from django.shortcuts import render,redirect
from .forms import Users
from .forms import UsersForm
from .forms import UpdateProfileForm
from django.contrib.auth.decorators import login_required
from .models import Users, Tutors, Playlist, Likes, Content, Bookmark, Comments
import hashlib
import os
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UsersForm

from django.contrib.auth import authenticate, login
from .forms import LoginForm



def degister(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неправильно заполнена'
            print(form.errors)  # добавить вывод ошибок формы в консоль
    else:
        form = UsersForm()
        print(form.errors)  # добавить вывод ошибок формы в консоль

    data = {'form': form, 'error': error}
    return render(request, 'applacation1/degister.html', data)





def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Неправильный email или пароль')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'applacation1/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')




def courses(request):
    return render(request,'applacation1/courses.html')



def home(request):
    return render(request,'applacation1/home.html')




def profile(request):
    user = request.user
    if not hasattr(user, 'id'):
        return redirect('login')

    total_likes = Likes.objects.filter(fk_pklikes_user_id=user.id).count()
    total_comments = Comments.objects.filter(fk_user_id=user.id).count()
    total_bookmarked = Bookmark.objects.filter(fk_user_id=user.id).count()

    return render(request, 'applacation1/profile.html', {
        'user': user,
        'total_likes': total_likes,
        'total_comments': total_comments,
        'total_bookmarked': total_bookmarked


    })



def login(request):
    return render(request,'applacation1/login.html')













def contact(request):
    return render(request,'applacation1/contact.html')




def dabout(request):
    return render(request,'applacation1/dabout.html')





def kuratori(request):
    return render(request,'applacation1/kuratori.html')






def playlist(request):
    return render(request,'applacation1/playlist.html')







def teacher_profile(request):
    return render(request,'applacation1/teacher_profile.html')







def watch_video(request):
    return render(request,'applacation1/watch_video.html')




def base(request):
    return render(request,'applacation1/base.html')







@login_required
def update(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')
            profile_picture = form.cleaned_data.get('profile_picture')

            if name:
                user.name = name
            if email:
                user.email = email

            if old_password and new_password and confirm_password:
                # Check if old password is correct
                if not user.check_password(old_password):
                    form.add_error('old_password', 'old password')
                    return render(request, 'application1/update.html', {'form': form})

                # Check if new password matches confirm password
                if new_password != confirm_password:
                    form.add_error('confirm_password', 'New passwords must match.')
                    return render(request, 'application1/update.html', {'form': form})

                user.set_password(new_password)

            if profile_picture:
                user.profile_picture = profile_picture

            user.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('update')

    else:
        form = UpdateProfileForm(initial=user)

    context = {'form': form}
    return render(request, 'applacation1/update.html', context)
