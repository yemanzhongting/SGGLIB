"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import xadmin
from django_web.views import index,BSweb,chart,file
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',index),
    url(r'BSweb/',BSweb),#修改了，后就是更新了一个引用，静态不需要mode曾
    url(r'^chart/', chart),
    url(r'file/',file),
    url(r'xadmin/',xadmin.site.urls),
    #url(r'somepath$', include('coconuts.urls')),
]
#html tag {}:format{}