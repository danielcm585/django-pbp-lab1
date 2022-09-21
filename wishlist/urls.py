from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', get_all_xml, name='get_all_xml'),
    path('json/', get_all_json, name='get_all_json'),
    path('xml/<int:id>', get_one_xml, name='get_one_xml'),
    path('json/<int:id>', get_one_json, name='get_one_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]