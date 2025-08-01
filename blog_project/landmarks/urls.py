from django.urls import path
from . import views
urlpatterns =[
    path('home/', views.home, name= 'home'),
    path('<int:id>/', views.landmark, name='single_place'),
    path('add/', views.add, name= 'add'),
    path('tag/<int:id>', views.filter_read, name= 'read'),
]