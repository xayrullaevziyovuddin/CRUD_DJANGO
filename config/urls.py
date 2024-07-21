
from django.contrib import admin
from django.urls import path
from mybook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:book_id>/delete/', views.book_del, name='book_del'),
    path('book/<int:book_id>/edit/', views.book_update, name='book_update'),
]
