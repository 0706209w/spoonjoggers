from django import forms
from pawcrastination.models import Picture, AnimalProfile, UserProfile
from pawcrastination.models import User
from pawcrastination.models import UserProfile
from django.template import RequestContext

class AnimalProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter your pets name!")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    animalType = forms.ChoiceField(choices = AnimalProfile.animalChoices)
    
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = AnimalProfile
		# Fields do we want to include in our form
        fields = ('name', 'animalType')

class PictureForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    caption = forms.CharField(max_length = 1024)
	
	# An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Picture
        # Fields do we want to include in our form
        fields = ('title', 'views', 'likes', 'caption', 'picture')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
	
	# An inline class to provide additional information on the form.
    class Meta:
		# Provide an association between the ModelForm and a model
        model = User
		# Fields do we want to include in our form
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

	# An inline class to provide additional information on the form.
    class Meta:
		# Provide an association between the ModelForm and a model
        model = UserProfile
		# Fields do we want to include in our form
        fields = ('picture',)
