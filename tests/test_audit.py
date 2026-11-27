# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Michele Salerno e i contributori di EduWISP
import pytest
from django.contrib.auth import get_user_model
from eduwisp_users.models import Organization

from eduwisp_audit.log import record
from eduwisp_audit.models import Action, AuditEvent

pytestmark = pytest.mark.django_db


@pytest.fixture
def admin_user():
    return get_user_model().objects.create_superuser("admin", password="x")


def test_registra_e_conserva_il_testo(admin_user):
    scuola = Organization.objects.create(name="Liceo Fittizio", slug="liceo")
    docente = get_user_model().objects.create_user("prof")
    ev = record(
        Action.VIEW_AS_START, actor=admin_user, organization=scuola, subject=docente, role="teacher"
    )
    docente.delete()
    scuola.delete()
    ev = AuditEvent.objects.get(pk=ev.pk)
    assert ev.subject is None and ev.subject_label == "prof"
    assert ev.organization is None and ev.organization_label == "Liceo Fittizio"
    assert ev.details == {"role": "teacher"}


def test_non_si_modifica_ne_si_cancella(admin_user):
    ev = record(Action.ACCESS_DENIED, actor=admin_user)
    ev.reason = "altro"
    with pytest.raises(PermissionError):
        ev.save()
    with pytest.raises(PermissionError):
        ev.delete()
    with pytest.raises(PermissionError):
        AuditEvent.objects.all().delete()
    with pytest.raises(PermissionError):
        AuditEvent.objects.update(reason="x")
    assert AuditEvent.objects.get().reason == ""


def test_admin_solo_lettura_e_solo_superuser(client, admin_user):
    ev = record(Action.ACCESS_DENIED, actor=admin_user)
    client.force_login(admin_user)
    assert client.get("/admin/eduwisp_audit/auditevent/").status_code == 200
    assert client.get(f"/admin/eduwisp_audit/auditevent/{ev.pk}/delete/").status_code == 403
    assert client.get("/admin/eduwisp_audit/auditevent/add/").status_code == 403
    staff = get_user_model().objects.create_user("staff", password="x", is_staff=True)
    client.force_login(staff)
    assert client.get("/admin/eduwisp_audit/auditevent/").status_code == 403
