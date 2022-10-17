from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [
    path('carousel', carousel, name='carousel'),
    path('carousel-add', carousel_add, name='carousel_add'),
    path('carousel-<int:pk>', carousel_single, name='carousel_single'),
    path('carousel-edit/<int:pk>', carousel_single_edit, name='carousel_single'),
]