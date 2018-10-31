from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('apps.accounts.urls')),
    url(r'^handyhelper/', include('apps.handyhelper.urls')),
]
