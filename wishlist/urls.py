from django.urls import path
from wishlist.views import get_all_json, get_all_xml, get_one_json, get_one_xml, show_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', get_all_xml, name='get_all_xml'),
    path('json/', get_all_json, name='get_all_json'),
    path('xml/<int:id>', get_one_xml, name='get_one_xml'),
    path('json/<int:id>', get_one_json, name='get_one_json'),
]