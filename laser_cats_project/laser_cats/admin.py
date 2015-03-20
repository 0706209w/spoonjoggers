from django.contrib import admin
from laser_cats.models import AnimalProfile
from laser_cats.models import Picture
from laser_cats.models import UserProfile

# Register your models here.

admin.site.register(AnimalProfile)
admin.site.register(Picture)
admin.site.register(UserProfile)
