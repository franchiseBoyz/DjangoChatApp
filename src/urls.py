from django.contrib import admin
from django.urls import path
from messenger.views import home_screen_view
from django.conf import settings
from django.conf.urls.static import static

from account.views import (
    register_view,

)

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('admin/', admin.site.urls),
    path('register/', register_view, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)