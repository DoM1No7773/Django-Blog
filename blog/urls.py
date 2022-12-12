from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/',views.detail,name='detail'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('login/',views.loginUser,name='login'),
    path('create/',views.createPost,name='create'),
    path('<int:post_id>/update/',views.updatePost,name='update'),
    path('<int:post_id>/delete/',views.deletePost,name='delete'),
]