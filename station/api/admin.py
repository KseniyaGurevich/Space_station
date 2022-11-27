from django.contrib import admin

from .models import Station, Instructions, User


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'date_creation', 'date_broken', 'x', 'y', 'z')


@admin.register(Instructions)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'axis', 'distance')


