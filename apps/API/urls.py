from django.urls import re_path
from . import views
 
urlpatterns = [ 
        re_path(r'^api/pets$', views.pet_list),
        re_path(r'^api/pets/(?P<pk>[0-9]+)$', views.pet_detail)
    ]