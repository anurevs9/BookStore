from django.urls import path
from . import views


urlpatterns = [
    path('',views.BookListView.as_view(),name='book_list'),
    path('book/<int:pk>/',views.BookDetailView.as_view(),name='book_details'),
    path('book/<int:pk>/edit/',views.BookUpdateView.as_view(),name='book_edit'),
    path('book/<int:pk>/delete/',views.BookDeleteView.as_view(),name='book_delete'),
    path('book/add/',views.BookCreateView.as_view(),name='book_add'),
]