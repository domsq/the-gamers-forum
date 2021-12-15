from django.urls import path
from . import views


urlpatterns = [
    path('', views.TopicList.as_view(), name='homepage'),
    path('topic/<str:name>/', views.TopicDetail.as_view(), name='topic_detail'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
