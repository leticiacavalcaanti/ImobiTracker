
from django.contrib import admin
from django.urls import path
from leads.views import leads


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', leads),
]
