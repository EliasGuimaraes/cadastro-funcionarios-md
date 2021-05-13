from django.contrib import admin
from registermd.models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('nome', 'cargo', 'publication_date')
    list_filter = ('nome', 'cargo')
    search_fields = ('nome', 'cargo')


admin.site.register(Publication, PublicationAdmin)

