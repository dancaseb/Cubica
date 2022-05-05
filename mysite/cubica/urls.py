from django.urls import path

from . import views 


app_name = 'cubica'
urlpatterns = [
   # path('', views.entry, name='entry'),
    path('latest/<int:post_id>/', views.detail, name='detail'),
    path('',views.index, name='index'),
    path('latest/',views.latest,name = 'latest'),
    #path('',views.mainpage, name='main'),
    path('logout/', views.logout, name='logout'),
]