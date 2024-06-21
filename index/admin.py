from django.contrib import admin
from .models import UserIP, Visit, About, Article, Comment, File


# Register your models here.

class UserIPAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_ip']}),
        (None, {'fields': ['access_time']}),
        (None, {'fields': ['serial_number']}),
        (None, {'fields': ['ip_attribution']}),
    ]
    list_display = ('serial_number', 'user_ip', 'ip_attribution', 'access_time')
    list_filter = ['access_time']
    search_fields = ['user_ip', 'ip_attribution']


admin.site.register(UserIP, UserIPAdmin)


class VisitAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date']}),
        (None, {'fields': ['visits']}),
        (None, {'fields': ['first_viewing_ip']}),
        (None, {'fields': ['latest_viewing_ip']}),
    ]
    list_display = ('date', 'visits', 'first_viewing_ip', 'latest_viewing_ip')
    search_fields = ['date']
    list_filter = ['date', 'first_viewing_ip', 'latest_viewing_ip']


admin.site.register(Visit, VisitAdmin)


class AboutAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
    ]
    list_display = ('title', 'pub_date')
    search_fields = ['title', 'content']
    list_filter = ['pub_date']

admin.site.register(About, AboutAdmin)


class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['author']}),
        (None, {'fields': ['category']}),
        (None, {'fields': ['state']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['mod_date'], 'classes': ['collapse']}),
        (None, {'fields': ['body']}),
    ]
    list_display = ('title', 'author', 'category', 'pub_date', 'state', 'latest_viewing_date', 'latest_viewing_user')
    list_filter = ['pub_date']
    search_fields = ['title', 'author', 'category', 'pub_date', 'body']


admin.site.register(Article, ArticlesAdmin)


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['author']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['ip']}),
        (None, {'fields': ['ip_attribution']}),
        ('Date information', {'fields': ['sub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['parent_id']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('id', 'author', 'email', 'ip', 'ip_attribution', 'sub_date', 'content', 'parent_id', 'delete')
    list_filter = ['sub_date']
    search_fields = ['author', 'content', 'email']


admin.site.register(Comment, CommentAdmin)


class FileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['file_name']}),
        (None, {'fields': ['file_size']}),
        (None, {'fields': ['pub_date']}),
        (None, {'fields': ['downloads']}),
    ]
    list_display = ('id', 'file_name', 'file_size', 'pub_date', 'downloads')
    list_filter = ['pub_date']
    search_fields = ['file_name', 'pub_date']


admin.site.register(File, FileAdmin)
