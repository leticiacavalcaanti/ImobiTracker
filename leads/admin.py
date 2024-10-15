from django.contrib import admin
from leads.models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','telefone',)
    list_display_links = ('id','nome',)
    list_per_page = 15
    search_fields = ('nome',)

admin.site.register(Lead, LeadAdmin)