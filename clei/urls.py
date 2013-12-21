from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('clei.apps.clei.urls')),
    url(r'^', include('clei.apps.SeleccionArticulos.urls')),
    url(r'^', include('clei.apps.inscripciones.urls')),
    url(r'^inscripcion/', include('clei.apps.inscripciones.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
