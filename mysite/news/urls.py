from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('category/<category_id>', get_category),
]