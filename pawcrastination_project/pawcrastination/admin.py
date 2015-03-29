from django.contrib import admin
from pawcrastination.models import AnimalProfile
from pawcrastination.models import Picture
from pawcrastination.models import UserProfile

# Register your models here.
admin.site.register(AnimalProfile)
admin.site.register(Picture)
admin.site.register(UserProfile)
