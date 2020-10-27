from django.contrib import admin
from django.urls import path, reverse

from . views import *

app_name = "user"
urlpatterns = [
    path('', UserListView.as_view(), name = 'user-list'),
    path('create/', UserCreateView.as_view(), name = 'user-create'),
    path('<int:pk>/', UserDetailView.as_view(), name = 'user-detail'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name = 'user-delete'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name = 'user-update'),

    #REST 
    path('users/', UserAPIList.as_view(), name = 'user-api-list'),
    path('users/<int:pk>/', UserAPIDetail.as_view(), name = 'user-api-detail'),

]
