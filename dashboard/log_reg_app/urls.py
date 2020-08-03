from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create, name="create"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]


    # path('success', views.success),