from django.urls import path, include
import sghouse.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', sghouse.views.home, name="home"),
    path('new/', sghouse.views.new, name="new"),
    path('detail/<int:index>', sghouse.views.detail, name="detail"),
    path('edit/<int:index>', sghouse.views.edit, name='edit'),
    path('detail/<int:pk>/delete', sghouse.views.delete, name="delete"),
    path('detail/<int:index>/comment/<int:comment_pk>/delete/', sghouse.views.delete_comment, name="delete_comment"),
    path('accounts/', include('accounts.urls')),
    path('class/', include('classli.urls')),
    path('mypage/', sghouse.views.mypage, name="mypage"),
    path('aboutservice/', sghouse.views.aboutservice, name="aboutservice"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)