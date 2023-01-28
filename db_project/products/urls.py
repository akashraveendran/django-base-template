from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_sample_page, name='view_sample_page'),
    path('sample', views.sample, name='sample'),
]