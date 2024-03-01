from django.contrib import admin
from django.urls import path,include
from . import views
from . import settings
from django.conf.url.static import static

urlpatterns = [
    path('',views.home,name='home')
] + static(settings.MEDIA_URL,document_root=MEDIA_ROOT)