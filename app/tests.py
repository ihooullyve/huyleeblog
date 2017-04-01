from django.test import TestCase

from app.models import Blog

class BlogTestCase(TestCase):
	def setUp(self):
		Blog.objects.create(title = "Test1" , content = "Test 2")

	def test_animals_can_speak(self):
		obj1 = Blog.objects.get(title = "Test1")
		print('HuyLee')
		print(obj1)
		self.assertEqual(str(obj1), 'Test1')
		print(self.assertEqual((obj1.title).lower(), 'test1'))
