from django.urls import path
from . import views


urlpatterns = [
    path('', views.TopicList.as_view(), name='homepage'),
    path('topic/<str:name>/', views.TopicDetail.as_view(), name='topic_detail'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add-post/', views.PostAdd.as_view(), name='add_post'),
    path('edit-post/<slug:slug>/', views.PostEdit.as_view(), name='edit_post'),
]
