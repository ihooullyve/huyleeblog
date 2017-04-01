from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
	TYPE_CHOICES = (
		('1', 'Male'),
		('0', 'Felmale'),
		)
	user = models.ForeignKey(User, null=True)
	gender = models.CharField(max_length=1, choices=TYPE_CHOICES, default=1)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)
	date = models.DateTimeField(default=datetime.now())
	avtar = models.ImageField(upload_to = '/avatar', default = '/avatar/no-img.jpg', null=True)

	def __str__(self):
		return u'%s'%self.user

class Blog(models.Model):
	title = models.CharField(max_length=200, null=True)
	content = models.TextField(null=True)
	user = models.ForeignKey(User, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)
	image = models.ImageField(upload_to = '', default = 'no-img.jpg')
	rate = models.IntegerField(default =0)

	def __str__(self):
		return u'%s'%self.title


class Comment(models.Model):
	fullname = models.CharField(max_length=45, null=True)
	comment = models.TextField(null=True)
	blog = models.ForeignKey(Blog, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)
	like = models.IntegerField(default =0)

	def __str__(self):
		return u'%s'%self.fullname

class ReplayComment(models.Model):
	comment = models.ForeignKey(Comment, null=True)
	fullname = models.CharField(max_length=45, null=True)
	reply = models.TextField()
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)
	like = models.IntegerField(default =0)

	def __str__(self):
		return u'%s'%self.comment
