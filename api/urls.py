from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [
    path('', home, name='home')
]