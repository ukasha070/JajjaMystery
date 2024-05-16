from django.contrib import admin

from .models import (Service, ServiceList)

from django.contrib import admin

class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    search_fields = ['title']
    list_filter = ['published']

admin.site.register(Service, ServiceModelAdmin)


class ServiceListModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    search_fields = ['title']  

admin.site.register(ServiceList, ServiceListModelAdmin)