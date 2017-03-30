"""zhess103 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from users.views import *

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^good/', include('goods.urls',namespace='good')),
    url(r'^user/', include('users.urls', namespace='user')),
    url(r'^order/', include('orders.urls', namespace='order')),
    url(r'^crm/', include('crm.urls', namespace='crm')),
    url(r'^finance/', include('finance.urls', namespace='finance')),

    url(r'^welcome/$', TemplateView.as_view(template_name="welcome.html"), name='welcome'),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
]
