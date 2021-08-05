from django.conf.urls import url
from . import views
from django.views.static import serve     
urlpatterns = [
        url(r'^static/(?P<path>.*)', serve, {'document_root':'/home/Dj/Django-of-Jestion-Nano/djangosite/static'}),     
	url(r'moments_input', views.moments_input),
#	url(r'', views.welcome),
]
 


