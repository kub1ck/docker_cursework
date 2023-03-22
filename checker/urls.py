from django.urls import path

from .views import *

urlpatterns = [
    path('', FilesListView.as_view(), name='files_list'),
    path('add_file/', AddFileView.as_view(), name='add_file'),
    path('detail_file/<int:pk>/', DetailFileView.as_view(), name='detail_file'),
    path('update_file/<int:pk>/', UpdateFileView.as_view(), name='update_file'),
    path('delete_file/<int:pk>/', DeleteFileView.as_view(), name='delete_file'),
]
