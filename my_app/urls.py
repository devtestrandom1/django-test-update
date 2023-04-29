from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.registerUser, name='register'),
    path('login', views.loginUser, name='login'),
    path('update-user', views.update_user, name='update-user')
]