from django.urls import path, include
from . import views

urlpatterns = [
    path('opencv_view/', views.opencv_view, name='opencv')
]
