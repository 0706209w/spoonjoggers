from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from laser_cats.forms import AnimalProfileForm, PictureForm, UserForm, UserProfileForm
from laser_cats.models import AnimalProfile, Picture
from datetime import datetime
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
# Create your views here.

def index(request):
    animalprofile_list = AnimalProfile.objects.order_by('-likes')[:5]
    context_dict = {'animalprofiles':animalprofile_list}
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


def animalprofile(request, animalprofile_name_slug):
    context_dict = {}

    try:
        if request.method == 'POST':
            pass
            # Can we find a animal profile name slug with the given name?
            # If we can't, the .get() method raises a DoesNotExist exception.
            # So the .get() method returns one model instance or raises an exception.
        animalprofile = AnimalProfile.objects.get(slug=animalprofile_name_slug)
        context_dict['animal_name'] = animalprofile.name
        context_dict['animalprofile_name_slug'] = animalprofile_name_slug

        # Retrieve all of the associated pictures.
        # Note that filter returns >= 1 model instance.
        pictures = Picture.objects.filter(user=animalprofile).order_by('-likes')

        # Adds our results list to the template context under name pages.
        context_dict['pictures'] = pictures
        # We also add the animal profile object from the database to the context dictionary.
        # We'll use this in the template to verify that the animalprofile exists.
        context_dict['animalprofile'] = animalprofile
    except AnimalProfile.DoesNotExist:
        # We get here if we didn't find the specified profile.
        # Don't do anything - the template displays the "no profile" message for us.
        pass

    
    return render(request, 'laser_cats/animalprofile.html', context_dict)
    
def add_Picture(request, animalprofile_name_slug):
    try:
        animal = AnimalProfile.objects.get(slug=animalprofile_name_slug)
    except AnimalProfile.DoesNotExist:
        animal = None
        
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            if animal:
                picture = form.save(commit = False)
                print picture
                print "1"
                picture.user = animal
                print "2"
                picture.views = 0
                picture.likes = 0
                print "3"
                picture.picture = request.FILES['picture']
                print picture.picture
                picture.save()
                
                return AnimalProfile(request, AnimalProfile_name_slug)
        else:
            print form.errors
    else:
        form = PictureForm()
        
    contect_dict = {'picture_form':form, 'animalprofile':animal, 'animalprofile_name_slug':animalprofile_name_slug}
    
    return render(request, 'laser_cats/add_picture.html', contect_dict)
                


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'laser_cats/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
                
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/lasercats/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Laser Cats account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'laser_cats/login.html', {})               

       
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!") 
    
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/lasercats/')
                
                
                
                
                
                
                
                
