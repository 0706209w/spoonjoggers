from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



# Create your models here.

class AnimalProfile(models.Model):
    name = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    owner = models.CharField(max_length=128)
	#"Dogs", "Cats", "Bunnies", "Horses", "Fish", "Birds", "Reptiles", "Others"]
    #choices
    DOG = 'Dogs'
    CAT = 'Cats'
    BUNNY = 'Bunnies'
    HORSE = 'Horses'
    FISH = 'Fish'
    BIRD = 'Birds'
    REPTILE = 'Reptiles'
    OTHER = 'Others' 

    animalChoices = (
        (DOG, 'Dogs'),
        (CAT, 'Cats'),
        (BUNNY, 'Bunnies'),
        (HORSE, 'Horses'),
        (FISH, 'Fish'),
        (BIRD, 'Birds'),
        (REPTILE, 'Reptiles'),
        (OTHER, 'Others'),
        )
    animalType = models.CharField(max_length=8, choices=animalChoices, default = OTHER)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(AnimalProfile, self).save(*args, **kwargs)

    def __unicode__(self):
            return self.name


class Picture(models.Model):
    caption = models.CharField(max_length = 1024)
    title = models.CharField(max_length = 64)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(AnimalProfile, default='')
    picture = models.ImageField(upload_to='images/', blank=True)
    #url = models.URLField()

    def __unicode__(self):
        return self.title



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to = 'profile_images', blank = True)

    def __unicode__(self):
        return self.user.username


    