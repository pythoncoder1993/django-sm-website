from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin-new', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('address', views.useraddressinformation, name='address'),
    path('world', views.helloworld, name='hello'),
    path('post', views.post, name='post'),
    path('article', views.article, name='article'),
    path('newposts', views.newposts, name='newposts')
]