from django.urls import path
from interpreter import views

urlpatterns = [
    path('', views.code_interpreter, name='code_interpreter')
]