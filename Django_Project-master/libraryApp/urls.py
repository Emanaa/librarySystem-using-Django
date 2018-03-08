from django.urls import path
from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views
app_name = 'libraryApp'

urlpatterns = [
	path('',views.listWriters,name='writers'),
    path('d/<int:writer_id>',views.writerDetails,name='detail'),
	path('signup', views.signup, name='signup'),
	path('login', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	path('x',views.x,name="x")
]
