from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logar, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('logout/', views.logout_view, name='logout'), 
    ]