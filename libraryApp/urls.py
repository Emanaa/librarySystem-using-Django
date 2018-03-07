from django.urls import path
from .libraryApp import views as core_views

from . import views
app_name = 'libraryApp'

urlpatterns = [
	path('',views.listWriters,name='writers'),
    path('d/<int:writer_id>',views.writerDetails,name='detail'),
	url(r'^signup/$', core_views.signup, name='signup')

]
