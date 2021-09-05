from django.urls import path
from .views import *

urlpatterns = [
    path('bboard/<int:rubric_id>/', by_rubric),
    path('', index),
]