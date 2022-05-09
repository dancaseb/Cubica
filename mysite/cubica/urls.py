from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views 


app_name = 'cubica'
urlpatterns = [
   # path('', viewss.entry, name='entry'),
    path('latest/<int:post_id>/', views.detail, name='detail'),
    path('',views.index, name='index'),
    path('latest/',views.latest,name = 'latest'),
    #path('',views.mainpage, name='main'),
    #####path('logout/', views.logout, name='logout'),
    path('groups/', views.groups, name='groups'),
    path('groups/<int:sub_id>/', views.group_detail, name='group_detail'),
    path('myprofile/',views.myprofile, name='myprofile'),
    path('latest/<int:post_id>/postcomment', views.postcomment, name='postcomment'),
    path('groups/<int:sub_id>/addpost', views.addpost, name='addpost'),
    path('groups/<int:sub_id>/addtogroup', views.addtogroup, name='addtogroup'),
    path('groups/<int:sub_id>/<int:post_id>/share', views.share, name='share'),
    path('profile/<int:person_id>',views.profile, name='profile'),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)