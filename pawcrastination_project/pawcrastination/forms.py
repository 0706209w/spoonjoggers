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
    #owner = forms.CharField(widget=forms.HiddenInput(), required=False)
    

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = AnimalProfile
        fields = ('name', 'animalType')


class PictureForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    caption = forms.CharField(max_length = 1024)
    
    

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Picture

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        #or specify the fields to include (i.e. not include the category field)
        fields = ('title', 'views', 'likes', 'caption', 'picture')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
