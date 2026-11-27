# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Michele Salerno e i contributori di EduWISP
from django.contrib import admin

from .models import AuditEvent


@admin.register(AuditEvent)
class AuditEventAdmin(admin.ModelAdmin):
    """Consultazione del registro: solo lettura e solo per gli amministratori di sistema."""

    list_display = ["created_at", "action", "actor_label", "subject_label", "organization_label"]
    list_filter = ["action"]
    search_fields = ["actor_label", "subject_label", "organization_label", "reason"]
    date_hierarchy = "created_at"

    def has_module_permission(self, request):
        return request.user.is_active and request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_active and request.user.is_superuser

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
