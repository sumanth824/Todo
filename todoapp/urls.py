from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('updatelist/<str:pk>/',views.updatelist,name='updatelist'),
    path('deletelist/<str:pk>/',views.deletelist,name='deletelist')
]