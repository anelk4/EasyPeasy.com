from django.shortcuts import render


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
    return render(request,'applacation1/degister.html')




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







def watchvideo(request):
    return render(request,'applacation1/watchvideo.html')




