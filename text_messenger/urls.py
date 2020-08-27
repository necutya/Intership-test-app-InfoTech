from django.urls import path
from . import views

urlpatterns = [
    path("", views.MessageViews.as_view(), name="home"),
    path("home/", views.MessageViews.as_view()),
    path("messages/", views.MessageViews.as_view()),
    path("about/", views.about, name="about"),
    path("new_message/", views.new_message, name="new_message"),
    path("messages/user/<pk>/", views.UserMessageViews.as_view(), name="user_messages"),
]
