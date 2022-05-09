from django.urls import path

from . import views

app_name = 'message'
urlpatterns = [
    path('', views.index, name='index'),
    path('sent/',views.sent,name='sent'),
    path('received/', views.received, name='received'),
    path('newmessage/<int:sub_id>/<int:post_id>', views.newmessage, name="newmessage"),
]