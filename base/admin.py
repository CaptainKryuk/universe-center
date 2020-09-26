from django.contrib import admin
from .models import SlideshowImage, SportSection, Coach


class SportSectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

# Register your models here.
admin.site.register(SlideshowImage)
admin.site.register(SportSection, SportSectionAdmin)
admin.site.register(Coach)