from django.contrib import admin
from django.urls import path , include
from resume.views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', include('resume.urls')),
    path('user/', include('user.urls')),
    path('', home),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)    