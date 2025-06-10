from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('update/<str:book_id>/', views.update_book, name='update_book'),
    path('delete/<str:book_id>/', views.delete_book, name='delete_book'),
]
