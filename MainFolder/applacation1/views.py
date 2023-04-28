from django.shortcuts import render,redirect
from .forms import Users
from .forms import UsersForm
from django.contrib.auth.decorators import login_required
from .models import Users, Tutors, Playlist, Likes, Content, Bookmark, Comments



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





def update(request):
    return render(request,'applacation1/update.html')







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




