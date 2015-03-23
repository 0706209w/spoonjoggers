import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'laser_cats_project.settings')

import django
django.setup()

from laser_cats.models import AnimalProfile, Picture, UserProfile

def populate():
    bob = add_user("bob", "email@legit.com", "password", "www.example.com", "profile_images/bobs_pretty_face.png")
    print "add user worked"
    print bob
    bobs_animal = add_animal("doge", owner = bob)
    print "add animal worked"
    print bobs_animal
    add_picture(animal = bobs_animal, caption = "this is a caption", title = "this is a title", picture = "images/quack.jpg")


def add_picture(animal, caption, title, picture, views=0, likes=0):
    p = Picture.objects.get_or_create(user = animal, caption = caption, title=title, likes=likes, views=views, picture = picture)
    return p

def add_animal(name, owner, views = 0, likes = 0):
    a = AnimalProfile.objects.get_or_create(name = name, owner = owner)[0]
    return a
    
#picture should be defined as a directory inside the media folder, so you will have to copy them manually for now :(
def add_user(username, email, password, website, picture):
    user =  django.contrib.auth.models.User(username = username, email=email, password = password)
    user.set_password(password)
    user.save()
    uprofile = UserProfile(user = user, website = website, picture = picture)
    uprofile.save()
    return uprofile

if __name__ == '__main__':
    print "Starting laser cats population script..."
    populate()

    
