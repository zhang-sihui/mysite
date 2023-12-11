from django.contrib import admin
from .models import UserIP, Visit, AboutSite, Article


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
    search_fields = ['ip_attribution']


admin.site.register(UserIP, UserIPAdmin)


class VisitAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date']}),
        (None, {'fields': ['visits']}),
    ]
    list_display = ('date', 'visits')
    search_fields = ['date']
    list_filter = ['date']


admin.site.register(Visit, VisitAdmin)


class AboutSiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
    ]
    list_display = ('title', 'pub_date')
    search_fields = ['title']
    list_filter = ['pub_date']

admin.site.register(AboutSite, AboutSiteAdmin)


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
    # list_display = ('title', 'author', 'category', 'pub_date', 'state')
    list_display = ('title', 'author', 'category', 'pub_date', 'state', 'latest_viewing_date', 'latest_viewing_user')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Article, ArticlesAdmin)
