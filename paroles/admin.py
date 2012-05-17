from paroles.models import Parole
from django.contrib import admin

class ParoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    actions = None

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.is_published():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.is_published():
            return False
        return True

    def queryset(self, request):
        return Parole.objects.not_published()

admin.site.register(Parole, ParoleAdmin)
