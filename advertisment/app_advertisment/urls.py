from django.urls import path 
from .views import index, pobeda

urlpatterns = [
    path('', index),
    path('start', pobeda)
]