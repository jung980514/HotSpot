from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.listData, name='listData'),
    path('writeData', views.writeData, name='writeData'),
    path('inputData', views.inputData, name='inputData'),
    path('editData', views.editData, name='editData'),
    path('updateData', views.updateData, name='updateData'),
    path('deleteData', views.deleteData, name='deleteData'),
]
