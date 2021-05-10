from django.urls import path, include
import accounts.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration/register/',accounts.views.register, name="register"),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/login/',auth_views.LoginView.as_view(),{'template_name':'login.html'},name="login"),
    path('registration/logged_out/',auth_views.LogoutView.as_view(),{'template_name':'logged_out.html'},name="logout"),
]