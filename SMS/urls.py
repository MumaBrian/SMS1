from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('teacher/', include('teacher.urls',)),
    path('adminn/', include('adminn.urls',)),
    path('student/',include('student.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(
    url_name="schema"), name="redoc",),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
    url_name="schema"), name="swagger-ui"),


]+ static(
settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
