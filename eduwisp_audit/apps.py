# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Michele Salerno e i contributori di EduWISP
from django.apps import AppConfig


class AuditConfig(AppConfig):
    name = "eduwisp_audit"
    verbose_name = "registro delle operazioni"
    default_auto_field = "django.db.models.BigAutoField"
