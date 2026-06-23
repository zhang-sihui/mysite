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
    list_display = ('serial_number', 'user_ip', 'ip_attribution', 'access_time')
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
        ('Date information', {'fields': ['create_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
    ]
    list_display = ('title', 'create_date')
    search_fields = ['title', 'content']
    list_filter = ['create_date']


admin.site.register(About, AboutAdmin)


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['create_date']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('name', 'create_date', 'delete')
    search_fields = ['name', 'delete']
    list_filter = ['create_date', 'delete']


admin.site.register(Author, AuthorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['create_date']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('name', 'create_date', 'delete')
    search_fields = ['name', 'delete']
    list_filter = ['create_date', 'delete']


admin.site.register(Category, CategoryAdmin)


class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['_author']}),
        (None, {'fields': ['_category']}),
        ('Date information', {'fields': ['create_date'], 'classes': ['collapse']}),
        ('Date information', {'fields': [
         'mod_date'], 'classes': ['collapse']}),
        (None, {'fields': ['body']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('id', 'title', 'author', 'category', 'create_date',
                    'latest_viewing_date', 'latest_viewing_user', 'delete')
    list_filter = ['create_date', 'delete']
    search_fields = ['title', 'author', 'category', 'create_date', 'body', 'delete']


admin.site.register(Article, ArticlesAdmin)


class FileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['file_name']}),
        (None, {'fields': ['file_size']}),
        (None, {'fields': ['create_date']}),
        (None, {'fields': ['downloads']}),
        (None, {'fields': ['create_user']}),
    ]
    list_display = ('id', 'file_name', 'file_size', 'create_date', 'downloads', 'create_user', 'delete')
    list_filter = ['create_date', 'delete']
    search_fields = ['file_name', 'create_date', 'create_user', 'delete']


admin.site.register(File, FileAdmin)


class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['creator']}),
        (None, {'fields': ['ip_attribution']}),
        ('Date information', {'fields': ['create_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['parent_id']}),
        (None, {'fields': ['delete']}),
    ]
    list_display = ('id', 'creator', 'ip_attribution', 'content', 'parent_id', 'create_date', 'delete')
    list_filter = ['create_date']
    search_fields = ['creator', 'content']


admin.site.register(Message, MessageAdmin)


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['password']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['create_date']}),
        (None, {'fields': ['delete']}),
    ]

    list_display = ('id', 'username', 'password', 'email', 'create_date', 'delete')
    list_filter = ['create_date']
    search_fields = ['username']


admin.site.register(User, UserAdmin)


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['creator']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['ip_attribution']}),
        (None, {'fields': ['article_id']}),
        (None, {'fields': ['create_date']}),
        (None, {'fields': ['delete']}),
    ]

    list_display = ('id', 'creator', 'content', 'ip_attribution', 'article_id', 'create_date', 'delete')
    list_filter = ['create_date']
    search_fields = ['content']


admin.site.register(Comment, CommentAdmin)


class ReplyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['creator']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['receiver']}),
        (None, {'fields': ['comment']}),
        (None, {'fields': ['ip_attribution']}),
        (None, {'fields': ['create_date']}),
        (None, {'fields': ['delete']}),
    ]

    list_display = ('id', 'creator', 'content', 'receiver', 'comment', 'ip_attribution', 'create_date', 'delete')
    list_filter = ['create_date']
    search_fields = ['content']


admin.site.register(Reply, ReplyAdmin)
