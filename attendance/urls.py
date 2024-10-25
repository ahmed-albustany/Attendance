from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_individual, name='register_individual'),
    path('create-course/', views.create_course, name='create_course'),
    path('waiting-list/', views.waiting_list, name='waiting_list'),
]