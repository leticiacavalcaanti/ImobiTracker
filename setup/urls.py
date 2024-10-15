
from django.contrib import admin
from django.urls import path, include
from leads.views import LeadsViewSet
from negocios.views import NegociosViewSet
from usuarios.views import UsuarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('leads', LeadsViewSet, basename='Leads')
router.register('negocios', NegociosViewSet, basename='Negocios')
router.register('usuarios', UsuarioViewSet, basename='Usuarios')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
