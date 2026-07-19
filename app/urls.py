from django.urls import path
from .views import UserList, UserView, UserCreate, UserUpdate, UserDelete, UserListCreate, UserDetail

urlpatterns = [
    path('users/', UserList, name='user-list'),
    path('users/<int:pk>/', UserView, name='user-detail'),
    path('users/create/', UserCreate, name='user-create'),
    path('users/update/<int:pk>/', UserUpdate, name='user-update'),
    path('users/delete/<int:pk>/', UserDelete, name='user-delete'),

    path('users-list-create/', UserListCreate, name='user-list-create'),
    path('users-detail/<int:pk>/', UserDetail, name='user-detail-crud'),
]