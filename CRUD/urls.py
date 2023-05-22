from django.urls import path
from . import views
from django.urls import re_path as url
 
#urlpatterns = [
#    path('',views.index,name='index'),
#    path('create',views.create,name="create"), 
#]
#from django.urls import path
#from . import views
#from django.conf.urls import url
 
urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name="create"),
    path('retrieve',views.retrieve,name="retrieve"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    url(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),  
]
