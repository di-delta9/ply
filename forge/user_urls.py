from django.urls import path,include
from forge import user_views
import ply
urlpatterns = [
    path('create/profile/',user_views.create_profile)
    
]
