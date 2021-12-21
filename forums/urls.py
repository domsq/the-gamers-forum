from django.urls import path
from . import views

# The PostDetail, PostEdit and delete_post URL paths
# adjusted following discussion with mentor

urlpatterns = [
    path('', views.TopicList.as_view(), name='homepage'),
    path('topic/<str:name>/', views.TopicDetail.as_view(),
         name='topic_detail'),
    path('post/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('add-post/', views.PostAdd.as_view(), name='add_post'),
    path('edit-post/<int:id>/', views.PostEdit.as_view(), name='edit_post'),
    path('delete-post/<int:id>/', views.delete_post, name='delete_post'),
]
