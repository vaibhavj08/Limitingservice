from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name = 'login'),
    path('signup/', views.signup,name = 'signup'),
    path('api_call/', views.api_call,name = 'api_call'),
    path('api_call/remaining_call/', views.remaining_call,name = 'remaining_call')
]