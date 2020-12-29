from django.urls import path
from five_two_one import views

urlpatterns = [
    path('', views.five_two_one, name='five_two_one'),
]