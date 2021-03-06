from django.contrib import admin
from .models import UserIP, EverydayVisit, AboutSite


# Register your models here.

class UserIPAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_ip']}),
        (None, {'fields': ['access_time']}),
        (None, {'fields': ['serial_number']}),
        (None, {'fields': ['ip_attribution']}),
    ]
    list_display = ('user_ip', 'access_time', 'serial_number', 'ip_attribution')
    list_filter = ['access_time']
    search_fields = ['ip_attribution']


admin.site.register(UserIP, UserIPAdmin)


class EverydayVisitAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date']}),
        (None, {'fields': ['visits']}),
    ]
    list_display = ('date', 'visits')
    search_fields = ['date']
    list_filter = ['date']


admin.site.register(EverydayVisit, EverydayVisitAdmin)

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
