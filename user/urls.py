from django.contrib import admin
from django.urls import path, reverse

from . views import *

app_name = "user"
urlpatterns = [
    path('', UserListView.as_view(), name = 'user-list'),
    path('create/', UserCreateView.as_view(), name = 'user-create'),
    path('<int:pk>/', UserDetailView.as_view(), name = 'user-detail'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name = 'user-delete'),
]
