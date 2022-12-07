from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("blog.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('myapi.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)