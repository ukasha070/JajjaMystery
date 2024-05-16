from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


handler404 = 'base.views.error_404_view'

urlpatterns = [
    path('jajja/', admin.site.urls),
    path("", include("base.urls"), name='base'),
    path("services/", include("service.urls"), name='services'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)