from django import template
from laser_cats.models import AnimalProfile

register = template.Library()

@register.inclusion_tag('laser_cats/cats.html')
def get_animalprofile_list():
	
    final_list= ["Dogs", "Cats", "Bunnies", "Horses", "Fish", "Birds", "Reptiles", "Others"]

    return {'cats': final_list}