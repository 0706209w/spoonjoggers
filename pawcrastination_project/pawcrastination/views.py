from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from pawcrastination.forms import AnimalProfileForm, PictureForm, UserForm, UserProfileForm
from pawcrastination.models import AnimalProfile, Picture, UserProfile
from datetime import datetime
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from datetime import datetime
from django.template.defaulttags import register
from django.template import RequestContext
# Create your views here.

def index(request):
    context_dict = {}
    animalprofile_list = AnimalProfile.objects.order_by('-likes')[:10]
    picture_list = Picture.objects.order_by('-likes')[:5]
    context_dict['animalprofiles'] = animalprofile_list
    context_dict['animalpictures'] = picture_list
    print context_dict
    return render(request, 'pawcrastination/index.html', context_dict)

def add_AnimalProfile(request):
    
    
	
    if request.method == 'POST':
        form = AnimalProfileForm(request.POST)

        if form.is_valid():
			
            profile = form.save(commit=False)
            profile.owner = request.user
            profile.save()
            return index(request)
        else:
            print form.errors
    else:
        form = AnimalProfileForm()

    return render(request, 'pawcrastination/add_animalprofile.html', {'form':form})


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
        #visits = int(request.COOKIES.get('visits', '1'))
        visits = request.session.get(animalprofile.name+'visits')
        if not visits:
            visits = 1
        reset_last_visit_time = False
        last_visit = request.session.get(animalprofile.name+'last_visit')
        if last_visit:
            print last_visit[:-7]
            last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
            if (datetime.now() - last_visit_time).seconds > 0:
                # ...reassign the value of the cookie to +1 of what it was before...
                visits = visits + 1
                # ...and update the last visit cookie, too.
                reset_last_visit_time = True
        else:
            # Cookie last_visit doesn't exist, so create it to the current date/time.
            reset_last_visit_time = True

        #Obtain our Response object early so we can add cookie information.
        response = render(request, 'pawcrastination/index.html', context_dict)
    
        if reset_last_visit_time:
            request.session[animalprofile.name+'last_visit'] = str(datetime.now())
            request.session[animalprofile.name+'visits'] = visits
            context_dict[animalprofile.name+'visits'] = visits
        
        if request.session.get(animalprofile.name+'visits'):
            count = request.session.get(animalprofile.name+'visits')
        else:
            count = 0
        response = render(request, 'pawcrastination/animalprofile.html', context_dict)
        
    except AnimalProfile.DoesNotExist:
        # We get here if we didn't find the specified profile.
        # Don't do anything - the template displays the "no profile" message for us.
        pass

    # Return response back to the user, updating any cookies that need changed
    return response
    
def add_Picture(request, animalprofile_name_slug):
    try:
        animal = AnimalProfile.objects.get(slug=animalprofile_name_slug)
    except AnimalProfile.DoesNotExist:
        animal = None
        
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
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
                context_dict = {'picture_form':form, 'animalprofile':animal, 'animalprofile_name_slug':animalprofile_name_slug}
                redirecturl = '/pawcrastination/animalprofile/' + animalprofile_name_slug
                return HttpResponseRedirect(redirecturl)
                #return AnimalProfile(request, animalprofile_name_slug)
        else:
            print form.errors
    else:
        form = PictureForm()
        
    context_dict = {'picture_form':form, 'animalprofile':animal, 'animalprofile_name_slug':animalprofile_name_slug}
    
    return render(request, 'pawcrastination/add_picture.html', context_dict)
                


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
            'pawcrastination/register.html',
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
                return HttpResponseRedirect('/pawcrastination/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Pawcrastination account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'pawcrastination/login.html', {})               

       
@login_required
def profile(request):
    context_dict = {}
    userprofile = request.user
    useranimals = AnimalProfile.objects.filter(owner=userprofile.username)
    context_dict['profile_name'] = userprofile.username
    context_dict['user_animals'] = useranimals
    animalprofile_list = AnimalProfile.objects.filter(owner=userprofile.username)
    context_dict = {'animalprofiles':animalprofile_list}
    user_object_list = UserProfile.objects.filter(user=userprofile)
    try:
		user_object = user_object_list[0]
		context_dict ['profileimageurl'] = user_object.picture.url
    except:
		context_dict ['profileimageurl'] = "/media/profile_images/default.jpg"
	
    return render(request, 'pawcrastination/profile.html', context_dict)
    #return HttpResponse("Since you're logged in, you can see this text!") 
    
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/pawcrastination/')
                
def add_like(animal_name):
    animalprofile.likes = animalprofile.likes+1
    return animalprofile           
                
                
def request_page(request):
  if(request.GET.get('mybtn')):
    add_like.add_like(animal_name)
  return render_to_response('pawcrastination/animalprofile.html')                
                
def track_url(request):
    context = RequestContext(request) 
    animalprofile_id = None 
    url = '/pawcrastination/animalprofile/' 
    if request.method == 'GET': 
        if 'animalprofile_id' in request.GET:
            animalprofile_id = request.GET['animalprofile_id']
            try: 
                
                #print AnimalProfile.objects.get()
                animalprofile = AnimalProfile.objects.get(id=animalprofile_id) 
             
                animalprofile.views = animalprofile.views + 1 
               
                animalprofile.save()
                
                
                url = url + animalprofile.slug + "/"
            except: 
                
                pass    
    return redirect(url)
	
def track_like(request):
    context = RequestContext(request) 
    animalprofile_id = None 
    url = '/pawcrastination/animalprofile/' 
    if request.method == 'GET': 
        if 'animalprofile_id' in request.GET:
            animalprofile_id = request.GET['animalprofile_id']
            try: 
                print "1"
                #print AnimalProfile.objects.get()
                animalprofile = AnimalProfile.objects.get(id=animalprofile_id) 
                print "2"
                animalprofile.likes = animalprofile.likes + 1 
                print "3"
                animalprofile.save()
                print "4"
                print url + animalprofile.slug
                url = url + animalprofile.slug + "/"
            except: 
                print "fail"
                pass    
    return redirect(url)

def track_plike(request):
    context = RequestContext(request) 
    picture_id = None 
    animalprofile_id = None 
    url = '/pawcrastination/animalprofile/' 
    if request.method == 'GET': 
        if 'picture_id' in request.GET:
            picture_id = request.GET['picture_id']
            try: 

        
                picture = Picture.objects.get(id=picture_id) 
             
                picture.likes = picture.likes + 1 
               
                picture.save()
                
      
                url = url + str(picture.user) + "/"

            except: 
                print "fail"
                pass   

    if request.method == 'GET': 
        if 'animalprofile_id' in request.GET:
            animalprofile_id = request.GET['animalprofile_id']
            try: 

                animalprofile = AnimalProfile.objects.get(id=animalprofile_id) 
   
                url = url + animalprofile.slug + "/"
				
            except: 
                print "fail"
                pass 				
    return redirect(url)              

def animal_type(request, typeofanimal):
    context_dict = {}
    useranimals = AnimalProfile.objects.filter(animalType=typeofanimal)
    context_dict['animalswithtype'] = useranimals
    context_dict['animaltype'] = typeofanimal
    #useranimals = AnimalProfile.objects.all()
    #useranimals2 = useranimals[3]
    #context_dict['user_animals'] = useranimals2.animalType
 
    return render(request, 'pawcrastination/animaltype.html', context_dict)
    #return HttpResponse("Since you're logged in, you can see this text!") 	