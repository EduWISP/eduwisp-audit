# Changelog — eduwisp-audit

## Non rilasciato / Unreleased

- Creazione del repository (fase di progettazione). / *Repository created (design phase).*
- Licenza AGPL-3.0-or-later con termini aggiuntivi (sezione 7), publiccode.yml e controllo DCO. / *AGPL-3.0-or-later licence with additional terms, publiccode.yml and DCO check.*
- Prototipo v0: registro delle operazioni in sola aggiunta (`AuditEvent`, `record()`), consultabile solo dagli amministratori di sistema; primo uso il «vedi come» (ADR-0018). / *v0 prototype: append-only audit log, superuser read-only admin; first used by "view as".*
- Evento `family_access_choice` ed eventi registrati da un dispositivo (`actor_label`), ADR-0018. / *`family_access_choice` event and device-originated events.*
- Eventi `app_unlock` e `app_unlock_end` per gli sblocchi temporanei delle app (ADR-0019). / *App unlock events.*
