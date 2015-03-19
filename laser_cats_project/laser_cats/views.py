from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from laser_cats.forms import AnimalProfileForm, PictureForm
from datetime import datetime
# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'wooooooooooooooo'}
    return render(request, 'laser_cats/index.html', context_dict)

def add_AnimalProfile(request):
    if request.method == 'POST':
        form = AnimalProfileForm(request.POST)

        if form.is_valid():
            form.save(commit=True)


            return index(request)
        else:
            print form.errors
    else:
        form = AnimalProfileForm()

    return render(request, 'laser_cats/add_animalprofile.html', {'form':form})


def AnimalProfile(request):

    return