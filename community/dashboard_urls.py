from django.urls import path,include
from community import dashboard_views

urlpatterns = [
    path('friends',dashboard_views.all_friends),
    #path('mentions',dashboard_views.all_mentions)
    #path('upload',dashboard_views.upload_content),
    path('api/',include('community.api_urls')),
    #path('upload/lighttable/',dashboard_views.upload_lighttable)
]
