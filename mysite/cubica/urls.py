from django.urls import path

from . import views 


app_name = 'cubica'
urlpatterns = [
   # path('', views.entry, name='entry'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('',views.index, name='index'),
]