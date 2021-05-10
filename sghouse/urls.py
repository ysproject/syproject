from django.urls import path
import sghouse.views

urlpatterns = [
    path('', sghouse.views.home, name="home"),
    path('new/', sghouse.views.new, name="new"),
    path('detail/<int:index>', sghouse.views.detail, name="detail"),
    path('edit/<int:index>', sghouse.views.edit, name='edit'),
    path('detail/<int:pk>/delete', sghouse.views.delete, name="delete"),
]