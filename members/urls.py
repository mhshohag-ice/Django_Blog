from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    #path('', views.index, name="index"),
    path('register/', UserRegisterView.as_view(), name="register"),

]