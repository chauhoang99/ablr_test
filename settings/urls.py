from django.contrib import admin
from django.urls import path

from myinfo_integration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='homepage'),
    path('auth/', views.myinfo_auth_view, name='auth'),
    path('callback/', views.myinfo_callback, name='callback')
]
