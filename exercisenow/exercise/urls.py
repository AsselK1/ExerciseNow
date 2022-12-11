# chat/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'exercise'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('challenge/', views.challenge, name='challenge'),
    path('subscription/', views.subscription, name='subscription'),
    path('shop/', views.shop, name='shop'),
    path('finish/', views.finish, name='finish'),
]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
