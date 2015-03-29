from django.test import TestCase
from django.core.urlresolvers import reverse
from pawcrastination.models import AnimalProfile, Picture, UserProfile

#Helper method
def add_AnimalProfile(name, views, likes):
	p = AnimalProfile.objects.get_or_create(name=name)[0]
	p.views = views
	p.likes = likes
	p.save()
	return p
	
#Helper method
def add_Picture(title, caption, views, likes, user_id):
	pict = Picture.objects.get_or_create(title=title, user_id=user_id)[0]
	pict.caption = caption
	pict.views = views
	pict.likes = likes
	pict.picture = "test picture"
	pict.save()
	return pict
	

class AnimalProfileModelTests(TestCase):
    def test_ensure_views_are_positive(self):
                aprof = AnimalProfile(name='test',views=-1, likes=0)
                aprof.save()
                self.assertEqual((aprof.views >= 0), True)
				
    def test_slug_line_creation(self):
				aprof = AnimalProfile(name='Test This',views=0, likes=0)
				aprof.save()
				self.assertEqual(aprof.slug, 'test-this')
				
    def test_ensure_likes_are_positive(self):
                aprof = AnimalProfile(name='test',views=0, likes=-1)
                aprof.save()
                self.assertEqual((aprof.likes >= 0), True)
				
				
class PictureModelTests(TestCase):
    def test_ensure_pictviews_are_positive(self):
                apict = Picture(title='test',views=1, likes=0, user_id = '1')
                apict.save()
                self.assertEqual((apict.views >= 0), True)
				
    def test_ensure_pictlikes_are_positive(self):
                apict = Picture(title='test',views=0, likes=1, user_id = '1')
                apict.save()
                self.assertEqual((apict.likes >= 0), True)
				
 
class IndexViewTests(TestCase):
    def test_index_view_with_no_profiles(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no pet profiles present.")
        self.assertQuerysetEqual(response.context['animalprofiles'], [])
		
    def test_index_view_with_profiles(self):
		add_AnimalProfile('test',1,1)
		add_AnimalProfile('test2',1,1)
		add_AnimalProfile('test3',1,1)
		add_AnimalProfile('test4',1,1)
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "test")
		num_profiles =len(response.context['animalprofiles'])
		self.assertEqual(num_profiles , 4)	
	
    def test_index_view_with_no_pictures(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no pet pictures present.")
        self.assertQuerysetEqual(response.context['animalpictures'], [])
	
	
class IndexViewTests2(TestCase):
	def test_index_view_with_pictures(self):
		add_Picture('test','test caption',1,1,'1')
		add_Picture('test2','test caption2',1,1,'1')
		add_Picture('test3','test caption3',1,1,'1')
		add_Picture('test4','test caption4',1,1,'1')
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "test caption")
		num_pictures =len(response.context['animalpictures'])
		self.assertEqual(num_pictures , 4)	

