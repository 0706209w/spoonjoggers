from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from datetime import datetime
# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'wooooooooooooooo'}
    return render(request, 'laser_cats/index.html', context_dict)