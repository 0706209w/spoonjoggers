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
    
def add_Picture(request, AnimalProfile_name_slug):
    try:
        animal = AnimalProfile.objects.get(slug=AnimalProfile_name_slug)
    except AnimalProfile.DoesNotExist:
        animal = None
        
    if request.method == 'POST':
        form - PictureForm(request.POST)
        if form.is_valid():
            if animal:
                picture = form.save(commit = False)
                picture.user = animal
                picture.views = 0
                picture.likes = 0
                picture.picture = request.FILES['picture']
                piture.save()
                return AnimalProfile(request, AnimalProfile_name_slug)
            else:
                print form.errors
        else:
            form = PictureForm()
            
        contect_dict = {'form':form, 'animalprofile':animal}
        
        return render(request, 'lasercats/add_picture.html', contect_dict)
                
                
                
                
                
                
                
                
                
                
                
                
                