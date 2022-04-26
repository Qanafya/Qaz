
from . import views
from django.contrib import admin
from django.urls import *
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('service/', views.service),
    path('contact/', views.contact),
    path('service/1/', views.ser1),
    path('service/2/', views.ser2),
    path('service/3/', views.ser3),
    path('admin/', admin.site.urls),
    path('users/', views.user),
    path('delete/<int:id>/', views.delete),
    path('edit/<int:id>/', views.edit),
    path('add/', views.add),
    path('std/', views.std),
    path('update/<int:id>', views.update),
    path('register/', views.registr),
    path('reg/', views.reg),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
