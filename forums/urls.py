from django.urls import path
from . import views


urlpatterns = [
    path('', views.TopicList.as_view(), name='homepage'),
]