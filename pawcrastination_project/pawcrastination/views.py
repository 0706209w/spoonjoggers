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
import string

# Index view
def index(request):
    context_dict = {}
	# Order the profiles by like count, top 10.
    animalprofile_list = AnimalProfile.objects.order_by('-likes')[:10]
    picture_list = Picture.objects.order_by('-likes')[:5]
    context_dict['animalprofiles'] = animalprofile_list
    context_dict['animalpictures'] = picture_list
    context_dict['host'] = request.get_host()
    print context_dict
    return render(request, 'pawcrastination/index.html', context_dict)
	
# View for adding an animal profile
def add_AnimalProfile(request):
    if request.method == 'POST':
        form = AnimalProfileForm(request.POST)
        if form.is_valid():
			# set current user as owner of animal profile
            profile = form.save(commit=False)
            profile.owner = request.user
            profile.save()
            return index(request)
        else:
            print form.errors
    else:
        form = AnimalProfileForm()
    return render(request, 'pawcrastination/add_animalprofile.html', {'form':form})

# View for Animal Profile	
def animalprofile(request, animalprofile_name_slug):
    context_dict = {}
	
	# Does the animal profile exist?
    try:
        if request.method == 'POST':
            pass
			
		# Retrieve information, save to context dictionary, to be used later.
        animalprofile = AnimalProfile.objects.get(slug=animalprofile_name_slug)
        context_dict['animal_name'] = animalprofile.name
        context_dict['animalprofile_name_slug'] = animalprofile_name_slug
        pictures = Picture.objects.filter(user=animalprofile).order_by('-likes')
        context_dict['pictures'] = pictures
        context_dict['animalprofile'] = animalprofile
        visits = request.session.get(animalprofile.name+'visits')
		
		# Is this the first time the page is viewed?
        if not visits:
            visits = 1
        reset_last_visit_time = False
        last_visit = request.session.get(animalprofile.name+'last_visit')
		
		# Has page been viewed previously? retrieve the date/time last of last visit. Update every 1 second.
        if last_visit:
            last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
            if (datetime.now() - last_visit_time).seconds > 1:
                visits = visits + 1
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
        # Template displays the "no profile" message for us.
        pass
    # Return response back to the user, updating any cookies that need changed
    return response
 
# View for adding Picture.
def add_Picture(request, animalprofile_name_slug):
	# Does the animal profile exist?
    try:
        animal = AnimalProfile.objects.get(slug=animalprofile_name_slug)
	# Animal profile does not exist?
    except AnimalProfile.DoesNotExist:
        animal = None    
	
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
			# If owner profile exists
            if animal:
				# Save information from form, initialize views/likes = 0. Update context dictionary.
                picture = form.save(commit = False)
                picture.user = animal
                picture.views = 0
                picture.likes = 0
                picture.picture = request.FILES['picture']
                picture.save()
                context_dict = {'picture_form':form, 'animalprofile':animal, 'animalprofile_name_slug':animalprofile_name_slug}
                redirecturl = '/pawcrastination/animalprofile/' + animalprofile_name_slug
                return HttpResponseRedirect(redirecturl)
				
		# If form is incorrect.
        else:
            print form.errors
    else:
        form = PictureForm()   
    context_dict = {'picture_form':form, 'animalprofile':animal, 'animalprofile_name_slug':animalprofile_name_slug}
    return render(request, 'pawcrastination/add_picture.html', context_dict)
 
# View for registering 
def register(request):
    # A check for successful registration
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Retrieve data from forms.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # Check for form validity.
        if user_form.is_valid() and profile_form.is_valid():
            # Save form and user data.
            user = user_form.save()
            # Hash password.
            user.set_password(user.password)
            user.save()
            # Pass through data to profile before saving.
            profile = profile_form.save(commit=False)
            profile.user = user
			# Check for uploaded picture.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Final save.
            profile.save()
            # Confirm success!
            registered = True
		# Form errors go here.
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'pawcrastination/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
			
# View for logging in               
def user_login(request):
    # If HTTP POST, Retrieve information.
    if request.method == 'POST':
        # Get username and password data from form.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Django magic to confirm correct credentials.
        user = authenticate(username=username, password=password)
        if user:
            # Active account check.
            if user.is_active:
                # log in!
                login(request, user)
                return HttpResponseRedirect('/pawcrastination/')
            else:
                # Inactive account - no logging in!
                return HttpResponse("Your Pawcrastination account is disabled.")
        else:
            # Bad login details.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'pawcrastination/login.html', {})               
 
# View for user profile
@login_required
def profile(request):
	# Create empty context dictionary
    context_dict = {}
	# Retrieve information, update context dictionary with data.
    userprofile = request.user
    useranimals = AnimalProfile.objects.filter(owner=userprofile.username)
    context_dict['profile_name'] = userprofile.username
    context_dict['user_animals'] = useranimals
    animalprofile_list = AnimalProfile.objects.filter(owner=userprofile.username)
    context_dict = {'animalprofiles':animalprofile_list}
    user_object_list = UserProfile.objects.filter(user=userprofile)
	# Check for associated profile image.
    try:
		user_object = user_object_list[0]
		context_dict ['profileimageurl'] = user_object.picture.url
	# If none, use default profile picture.
    except:
		context_dict ['profileimageurl'] = "/media/profile_images/default.jpg"
    return render(request, 'pawcrastination/profile.html', context_dict)

# View for logging out.
@login_required
def user_logout(request):
    # Log out user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect('/pawcrastination/')      
                
# View for like button                
def request_page(request):
# If like button is pressed, increment like.
  if(request.GET.get('mybtn')):
    add_like.add_like(animal_name)
  return render_to_response('pawcrastination/animalprofile.html')                

# View for tracking amount of views of page.  
def track_url(request):
    context = RequestContext(request) 
    animalprofile_id = None 
    url = '/pawcrastination/animalprofile/' 
    if request.method == 'GET': 
        if 'animalprofile_id' in request.GET:
            animalprofile_id = request.GET['animalprofile_id']
            try:
				# Update view count.
                animalprofile = AnimalProfile.objects.get(id=animalprofile_id) 
                animalprofile.views = animalprofile.views + 1 
				# Save profile updates.
                animalprofile.save()
                url = url + animalprofile.slug + "/"
            except: 
                pass    
    return redirect(url)

# View for animal profile likes.	
def track_like(request):
    context = RequestContext(request) 
    animalprofile_id = None 
    url = '/pawcrastination/animalprofile/' 
    if request.method == 'GET': 
        if 'animalprofile_id' in request.GET:
            animalprofile_id = request.GET['animalprofile_id']
            try: 
				# Find correct animal profile.
                animalprofile = AnimalProfile.objects.get(id=animalprofile_id) 
				# Increment likes by 1.
                animalprofile.likes = animalprofile.likes + 1 
				# Save updated profile.
                animalprofile.save()
				# prepare url to redirect back to same page.
                url = url + animalprofile.slug + "/"
            except: 
                pass    
	# Go to url.
    return redirect(url)

# view for animal picture likes.
def track_plike(request):
    context = RequestContext(request) 
    picture_id = None 
    url = '/pawcrastination/animalprofile/' 
    if request.method == 'GET': 
        if 'picture_id' in request.GET:
            picture_id = request.GET['picture_id']
            try: 
				# Find correct picture.
                picture = Picture.objects.get(id=picture_id) 
				# Increment likes by 1.
                picture.likes = picture.likes + 1 
				# Save updated picture.
                picture.save()
				# Format name of picture owner to fit with url
                x = str(picture.user)
                x = x.lower()
                x = x.replace(" ", "-")
				# Construct url.
                url = url + x + "/"
            except: 
                print "fail"
                pass   
    if request.method == 'GET': 
        if 'animalprofile_id' in request.GET:
            animalprofile_id = request.GET['animalprofile_id']
            try: 
				# Fetch corresponding animal profile.
                animalprofile = AnimalProfile.objects.get(id=animalprofile_id) 
				# construct url.
                url = url + animalprofile.slug + "/"
            except: 
                print "fail"
                pass 
	# Go to url.
    return redirect(url)              

# View for filtering by animal type.
def animal_type(request, typeofanimal):
	# Create empty context dictionary for info.
    context_dict = {}
	# Filter and update context dictionary with animaltype key, and animals that belong.
    useranimals = AnimalProfile.objects.filter(animalType=typeofanimal)
    context_dict['animalswithtype'] = useranimals
    context_dict['animaltype'] = typeofanimal
    return render(request, 'pawcrastination/animaltype.html', context_dict)
