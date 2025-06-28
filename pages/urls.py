from django.urls import path
from .views import (
    PageListView, PageDetailView, about_view,
    PageCreateView, PageUpdateView,
    delete_comment, edit_comment
)

urlpatterns = [
    path('', PageListView.as_view(), name='home'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('pages/<int:pk>/edit/', PageUpdateView.as_view(), name='page_edit'),
    path('pages/new/', PageCreateView.as_view(), name='page_create'),
    path('about/', about_view, name='about'),
    path('comments/<int:pk>/delete/', delete_comment, name='comment_delete'),
    path('comments/<int:pk>/edit/', edit_comment, name='edit_comment'),
]
