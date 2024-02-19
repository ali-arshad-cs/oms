from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('orphans/', include('orphans.urls')),
    path('guardians/', include('guardians.urls', namespace='guardians')),
    #path('leaves/', include('leaves.urls', namespace='leaves')),
    path('', include('employees.urls')),
    path('members/', include('members.urls', namespace='members')),
    path('volunteers/', include('volunteer.urls', namespace='volunteers')),
    path('marketing/', include('marketing.urls', namespace='marketing')),
]
handler404 = 'authentication.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

