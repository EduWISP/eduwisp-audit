# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Michele Salerno e i contributori di EduWISP
"""Registro delle operazioni amministrative, in sola aggiunta.

Gli eventi non si modificano e non si cancellano dall'applicazione. Chi agisce, l'istituto e la
persona coinvolta sono collegati e, in più, copiati come testo: l'evento resta leggibile anche
se l'utente o l'istituto vengono cancellati (per esempio quando si ricrea la demo).
"""

from django.conf import settings
from django.db import models


class Action(models.TextChoices):
    VIEW_AS_START = "view_as_start", "inizio «vedi come»"
    VIEW_AS_STOP = "view_as_stop", "fine «vedi come»"
    ACCESS_DENIED = "access_denied", "accesso negato"
    FAMILY_ACCESS_CHOICE = "family_access_choice", "scelta sull'accesso dei familiari"


class ReadOnlyQuerySet(models.QuerySet):
    def update(self, **kwargs):
        raise PermissionError("Il registro delle operazioni non si modifica.")

    def delete(self):
        raise PermissionError("Il registro delle operazioni non si cancella.")


class AuditEvent(models.Model):
    created_at = models.DateTimeField("quando", auto_now_add=True, db_index=True)
    action = models.CharField("operazione", max_length=40, choices=Action.choices)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        verbose_name="chi",
    )
    actor_label = models.CharField("chi (testo)", max_length=150)
    organization = models.ForeignKey(
        "eduwisp_users.Organization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        verbose_name="istituto",
    )
    organization_label = models.CharField("istituto (testo)", max_length=200, blank=True)
    subject = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        verbose_name="persona coinvolta",
    )
    subject_label = models.CharField("persona coinvolta (testo)", max_length=150, blank=True)
    reason = models.TextField("motivo", blank=True)
    details = models.JSONField("dettagli", default=dict, blank=True)

    objects = ReadOnlyQuerySet.as_manager()

    class Meta:
        verbose_name = "evento"
        verbose_name_plural = "registro delle operazioni"
        ordering = ["-created_at", "-id"]

    def __str__(self):
        return f"{self.created_at:%Y-%m-%d %H:%M} {self.actor_label}: {self.get_action_display()}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            raise PermissionError("Il registro delle operazioni non si modifica.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise PermissionError("Il registro delle operazioni non si cancella.")
