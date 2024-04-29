from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home_view(request):
    return render(request, 'Home.html')


def login_view(request):
    return render(request, 'Login_Page.html')


def signup_view(request):
    return render(request, 'signup.html')

def driving_view(request):
    return render(request, 'driver.html')


def aboutus(request):
    return render(request, 'About.html')


def categorise(request):
    return render(request, 'categorise.html')


def categorise_carwash(request):
    return render(request, 'carwash.html')


def categorise_computer(request):
    return render(request, 'computer.html')


def categorise_cleaning(request):
    return render(request, 'cleaning.html')


def categorise_interior(request):
    return render(request, '')


def categorise_homemaid(request):
    return HttpResponse('<h1 align="center">Home maid related work will appear here </h1>')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/home/')

    form = UserCreationForm()
    context={
        'register_form' : form,
    }
    return render(request, 'test.html',context)










