from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('writers/', views.writers, name='writers'),
    path('writers/<str:author_name>/', views.author_detail, name='author_detail'),
    path('books/', views.books, name='books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('writers/', views.writers_info, name='writers_info'),
]
