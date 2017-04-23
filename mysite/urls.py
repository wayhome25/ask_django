# mysite/urls.py

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^dojo/', include('dojo.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
