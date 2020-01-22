from django.conf.urls import  include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#         (r'^myapp/', include('myapp.urls')),
#         (r'^$', 'myapp.views.index'),
#         (r'^admin/', include(admin.site.urls)),

# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^myapp/', include('myapp.urls')),
    url(r'^$', 'myapp.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
