from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('book/',views.get_all_books),
    path('book/detail/<int:book_id>/',views.detail_book),
    path('book/create/',views.add_book),
    path('book/update/<int:book_id>/',views.update_book),
    path('book/delete/<int:book_id>/',views.delete_book)
]
