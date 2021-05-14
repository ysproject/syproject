from django.urls import path, include
import classli.views

urlpatterns = [
    path('class/classhome/',classli.views.classhome, name="classhome"),
]