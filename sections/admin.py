from django.contrib import admin
from sections.models import Section, Section_completed,Available_sections

admin.site.register(Section)
admin.site.register(Section_completed)
admin.site.register(Available_sections)

# Register your models here.
