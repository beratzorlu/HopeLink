from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('more_info/<int:ngo_id>/', views.ngo_detail_views, name='detail_view'),
    path('read_blog/<int:blog_id>/', views.blog_detail_views, name='blog_view'),
    path('search/', views.search, name='search'),
]
