from django.contrib import admin
from .models import Profile, Blog, Comment, ReplayComment

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'gender', 'date', 'updated']

class BlogAdmin(admin.ModelAdmin):
	list_display = ['user', 'title', 'rate', 'updated']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['blog','fullname', 'comment', 'like', 'updated']

class ReplayCommentAdmin(admin.ModelAdmin):
	list_display = ['comment', 'reply', 'fullname', 'like', 'updated']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplayComment, ReplayCommentAdmin)
