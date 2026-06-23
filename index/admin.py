from django.contrib import admin
from .models import IP, Visit, About, Article, File, Author, Category, Message, User, Comment, Reply

# Register your models here.


class IPAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_ip']}),
        (None, {'fields': ['access_time']}),
        (None, {'fields': ['serial_number']}),
        (None, {'fields': ['ip_attribution']}),
    ]
    list_display = ('serial_number', 'user_ip',
                    'ip_attribution', 'access_time')
    list_filter = ['access_time']
    search_fields = ['user_ip', 'ip_attribution']


admin.site.register(IP, IPAdmin)


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
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
    ]
    list_display = ('title', 'pub_date')
    search_fields = ['title', 'content']
    list_filter = ['pub_date']


admin.site.register(About, AboutAdmin)


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['created_date']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('name', 'created_date', 'delete')
    search_fields = ['name', 'delete']
    list_filter = ['created_date', 'delete']


admin.site.register(Author, AuthorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['created_date']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('name', 'created_date', 'delete')
    search_fields = ['name', 'delete']
    list_filter = ['created_date', 'delete']


admin.site.register(Category, CategoryAdmin)


class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['_author']}),
        (None, {'fields': ['_category']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
        ('Date information', {'fields': [
         'mod_date'], 'classes': ['collapse']}),
        (None, {'fields': ['body']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('id', 'title', 'author', 'category', 'pub_date',
                    'latest_viewing_date', 'latest_viewing_user', 'delete')
    list_filter = ['pub_date', 'delete']
    search_fields = ['title', 'author',
                     'category', 'pub_date', 'body', 'delete']


admin.site.register(Article, ArticlesAdmin)


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


class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['creator']}),
        (None, {'fields': ['ip_attribution']}),
        ('Date information', {'fields': [
         'created_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['parent_id']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('id', 'creator', 'ip_attribution',
                    'content', 'parent_id', 'created_date', 'delete')
    list_filter = ['created_date']
    search_fields = ['creator', 'content']


admin.site.register(Message, MessageAdmin)


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['password']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['created_date']}),
        (None, {'fields': ['delete']}),
    ]

    list_display = ('id', 'username', 'password',
                    'email', 'created_date', 'delete')
    list_filter = ['created_date']
    search_fields = ['username']


admin.site.register(User, UserAdmin)


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['creator']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['ip_attribution']}),
        (None, {'fields': ['article_id']}),
        (None, {'fields': ['created_date']}),
        (None, {'fields': ['delete']}),
    ]

    list_display = ('id', 'creator', 'content', 'ip_attribution',
                    'article_id', 'created_date', 'delete')
    list_filter = ['created_date']
    search_fields = ['content']


admin.site.register(Comment, CommentAdmin)


class ReplyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['creator']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['receiver']}),
        (None, {'fields': ['comment']}),
        (None, {'fields': ['ip_attribution']}),
        (None, {'fields': ['created_date']}),
        (None, {'fields': ['delete']}),
    ]

    list_display = ('id', 'creator', 'content', 'receiver',
                    'comment', 'ip_attribution', 'created_date', 'delete')
    list_filter = ['created_date']
    search_fields = ['content']


admin.site.register(Reply, ReplyAdmin)
