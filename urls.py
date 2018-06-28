from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from notes.api import NoteViewset, PersonalNoteViewset
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'notes', NoteViewset)
router.register(r'personal_notes', PersonalNoteViewset)




urlpatterns = [
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
]