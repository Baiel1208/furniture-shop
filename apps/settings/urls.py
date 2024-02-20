from django.urls import path

from apps.settings import views

urlpatterns = [
    path('', views.index, name='index'),

]