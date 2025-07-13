from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    # path('test_data', views.class_data,name = 'test_data'),
    path('update_data', views.update_data, name = 'update_data'),
    path('view_data', views.view_data, name = 'view_data'),

]
