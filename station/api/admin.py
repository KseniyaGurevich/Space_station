from django.contrib import admin

from .models import Station, Instructions, StationInstruction


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'date_creation', 'date_broken')


@admin.register(Instructions)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'axis', 'distance')


@admin.register(StationInstruction)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'station', 'instruction')