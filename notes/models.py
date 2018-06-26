from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable= False)
    #TODO: Add user/author who created it
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    

    
    #TODO Tagging system or categories
    category = models.CharField(max_length=20)


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
class Bookmarks(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid4, editable= False)
  # url = models.UrlField(max_length=200)    
   title = models.CharField(max_length=100)
   date_added = models.DateTimeField(auto_now=True)