from django.shortcuts import render,redirect
from .forms import Users
from .forms import UsersForm

def courses(request):
    return render(request,'applacation1/courses.html')



def home(request):
    return render(request,'applacation1/home.html')



def profile(request):
    return render(request,'applacation1/profile.html')



def login(request):
    return render(request,'applacation1/login.html')



def update(request):
    return render(request,'applacation1/update.html')




def degister(request):
    error=''
    if request.method=='POST':
        form=UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма неправльно заполнено'

    form=UsersForm()
    data={'form':form,
          'error':error

    }
    return render(request,'applacation1/degister.html',data)




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




