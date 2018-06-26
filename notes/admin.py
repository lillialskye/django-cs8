from django.contrib import admin
from .models import Note, PersonalNote, Bookmarks

# Register your models here.
admin.site.register(Note)
admin.site.register(PersonalNote)
admin.site.register(Bookmarks)