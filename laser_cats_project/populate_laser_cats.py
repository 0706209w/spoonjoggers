import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'laser_cats_project.settings')

import django
django.setup()

from laser_cats.models import AnimalProfile, Picture

def populate():
    bob_animal = add_animal('Bob')

    add_picture(animal = bob_animal, caption = "hurrdurr imma dog", title = "no")

def add_picture(animal, caption, title, views=0, likes=0):
    p = Picture.objects.get_or_create(user = animal, caption = caption, title=title, likes=likes, views=views)
    return p

def add_animal(name):
    a = AnimalProfile.objects.get_or_create(name = name)[0]
    return a

if __name__ == '__main__':
    print "Starting laser cats population script..."
    populate()

    
