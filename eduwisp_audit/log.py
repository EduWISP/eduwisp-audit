# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Michele Salerno e i contributori di EduWISP
"""Funzione da usare negli altri moduli per registrare un'operazione."""

from .models import AuditEvent


def record(
    action, *, actor, organization=None, subject=None, reason="", actor_label=None, **details
):
    """Registra un evento e lo restituisce. Non salva mai password o contenuti delicati.

    ``actor`` può essere ``None`` quando agisce un dispositivo: in quel caso ``actor_label``
    lo descrive (per esempio «dispositivo TAB-0001»).
    """
    return AuditEvent.objects.create(
        action=action,
        actor=actor,
        actor_label=actor_label or (actor.get_username() if actor else ""),
        organization=organization,
        organization_label=str(organization) if organization else "",
        subject=subject,
        subject_label=subject.get_username() if subject else "",
        reason=reason,
        details=details,
    )
