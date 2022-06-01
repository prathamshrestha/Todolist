from django.urls import path

from .views import register_view,login_view,user_view,logout_view

urlpatterns = [
    path('register/',register_view.as_view()),
    path('login/',login_view.as_view()),
    path('user/',user_view.as_view()),
    path('logout/',logout_view.as_view())


]