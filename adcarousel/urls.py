"""
URL configuration for adcarousel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.adcarousel),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('adcarousel/new/', views.adcarousel_create, name='adcarousel_create'),  # 新增路由
    
    path('adcarousel/<str:id>/', views.adcarousel_detail, name='adcarousel_detail'),
    path('adcarousel/<str:id>/update/', views.adcarousel_update, name='adcarousel_update'),
    path('adcarousel/<str:id>/delete/', views.delete_adcarousel, name='delete_adcarousel'),
    path('adcarousel/<str:id>/preview/', views.adcarousel_preview, name='adcarousel_preview'),
    path('adcarousels/play/', views.adcarousel_list_play, name='adcarousel_list_play'),
    path('adcarousel/<str:id>/toggle_is_selected/', views.toggle_is_selected, name='toggle_is_selected'),
    path('adcarousel/<str:id>/update_orderkey/', views.update_orderkey, name='update_orderkey'),
    path('adcarousel/<str:id>/update_fontcolor/', views.update_fontcolor, name='update_fontcolor'),
    path('adcarousel/<str:id>/update_fontsize/', views.update_fontsize, name='update_fontsize'),
    path('adcarousel/<str:id>/update_fontposition/', views.update_fontposition, name='update_fontposition'),
    path('adcarousel/<str:id>/update_showtimeout/', views.update_showtimeout, name='update_showtimeout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
