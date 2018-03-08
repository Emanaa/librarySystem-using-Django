from django.urls import path
from django.conf.urls import url
from .libraryApp import views as core_views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views
app_name = 'libraryApp'

urlpatterns = [
	path('',views.listWriters,name='writers'),
    path('d/<int:writer_id>',views.writerDetails,name='detail'),
	url(r'^signup/$', core_views.signup, name='signup'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]
