from .views import*
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register(r'customers',customerviews,basename='customers')




urlpatterns = [
    
    path('',include(router.urls))

]
