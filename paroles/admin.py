# -*- coding: utf-8 -*-

from paroles.models import Parole
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

class IsPublishedListFilter(SimpleListFilter):
    title = 'Etat'
    parameter_name = 'published'

    def lookups(self, request, model_admin):
        return (
            ('true', 'Publié'),
            ('false', 'Non publié'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'true':
            return Parole.objects.published()
        if self.value() == 'false':
            return Parole.objects.not_published()

class ParoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = (IsPublishedListFilter,)
    actions = None

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.is_published():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.is_published():
            return False
        return True

admin.site.register(Parole, ParoleAdmin)
