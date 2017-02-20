"""swipes URL Configuration

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
from selling import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.list_post, name="create"),
    url(r'^detail$', views.view_post, name="detail"),
    url(r'^delete/(?P<id>\d+)/$', views.delete_post, name="delete"),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^api/posts$', views.PostList.as_view()),
    url(r'^api/posts/(?P<pk>\d+)$', views.PostDetail.as_view()),
    url(r'^api/postdates$', views.PostDateList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)