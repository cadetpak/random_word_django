
from django.conf.urls import include, url 
from django.contrib import admin

urlpatterns = [
	url(r'^$', include('apps.generator.urls')),
	url(r'^generate/', include('apps.generator.urls')),
	url(r'^destroy/', include('apps.generator.urls')),
    url(r'^admin/', admin.site.urls),
]
