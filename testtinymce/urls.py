from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import include, url

import tinymce.urls

admin.autodiscover()

urlpatterns = [
    url(r'^tinymce/', include(tinymce.urls)),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
