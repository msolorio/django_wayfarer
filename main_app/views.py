from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

def signup(request):
    # if form submited on signup page
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save() # saves new user in db
            login(request, user) # login user
            Profile.objects.create(user=user) # creates profile for user

            return redirect('cities_index') # redirect to cities/
    
    # if navigate to signup page
    else:
        form = UserCreationForm()
        # display form for signup
        return render(request, 'registration/signup.html', { 'form': form })


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')