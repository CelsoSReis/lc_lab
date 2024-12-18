from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios import views
#URLs do Sistema
urlpatterns = [
    path('', views.logar, name="logar"),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('exames/', include('exames.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
