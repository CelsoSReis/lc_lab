from django.contrib import admin
from django.urls import path, include
#URLs do Sistema
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('exames/', include('exames.urls')),
]
