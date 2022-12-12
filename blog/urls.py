from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/',views.detail,name='detail'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('login/',views.loginUser,name='login'),
]