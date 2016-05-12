from django.contrib import admin
from frontend.models import Release


class ReleaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Release, ReleaseAdmin)
