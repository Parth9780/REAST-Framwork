from django.contrib import admin
from django.urls import path,include
from API import views
from .views import getid
from .views import deleteid
from .views import savedata


urlpatterns = [
    path('',views.getall),
    path('getid/<int:id>/', getid, name='getid'),
    path('deleteid/<int:id>/', deleteid, name='deleteid'),
    path('savedata/', savedata, name='savedata'),
    path('updateid/<int:id>',views.updateid),
]