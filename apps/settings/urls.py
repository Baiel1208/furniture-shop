from django.urls import path

from apps.settings import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('error/', views.error, name='error'),

]