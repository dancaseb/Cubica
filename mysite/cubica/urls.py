from django.urls import path

from . import views 


app_name = 'cubica'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
]