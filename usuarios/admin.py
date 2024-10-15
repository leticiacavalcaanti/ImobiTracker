from django.contrib import admin
from usuarios.models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nivelDeAcesso','nome','login','senha','creci','cargo',)
    list_display_links = ('id','nome',)
    list_per_page = 15
    search_fields = ('nome',)

admin.site.register(Usuario, UsuarioAdmin)

