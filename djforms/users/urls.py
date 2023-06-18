from django.urls import path
from .views import user_list, create_user

app_name = 'users'

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create/', create_user, name='create_user'),
]
