# Privacy — eduwisp-audit

Documento vivo: va aggiornato a ogni modifica che riguarda dati personali. Riferimenti: [Quadro normativo](https://eduwisp.org/docs/sicurezza-privacy/quadro-normativo/), [Requisiti di conformità](https://eduwisp.org/docs/requisiti/requisiti/#requisiti-di-conformità).

## Dati personali previsti

- Eventi amministrativi: chi, cosa, quando, motivazione.
- Riferimenti a utenti e dispositivi coinvolti.
- Attenzione: i log sul personale ricadono nell'art. 4 dello Statuto dei lavoratori (RC-010).

## Prototipo v0

- Il registro è **in sola aggiunta**: l'applicazione non permette di modificare o cancellare gli eventi, nemmeno all'amministratore. La pulizia a fine conservazione sarà un comando separato, da progettare.
- Si registrano solo i dati necessari: mai password, contenuti delle pagine viste o dati degli studenti.
- Primo uso: il «vedi come» dell'amministratore (ADR-0018).

## Trattamenti

| Dato | Finalità | Base giuridica | Conservazione | Chi vi accede |
|---|---|---|---|---|
| Eventi del registro (chi, operazione, istituto, persona coinvolta, motivo, quando) | sicurezza e verificabilità degli accessi degli amministratori (GDPR art. 5.2 e 32; provvedimento del Garante sugli amministratori di sistema del 27/11/2008) | obbligo legale (art. 6.1.c) | almeno 6 mesi per gli accessi degli amministratori di sistema; durata massima da definire con il DPO | solo gli amministratori di sistema, in sola lettura |

---

🇬🇧 *Expected personal data:*

- *Administrative events: who, what, when, reason.*
- *References to users and devices involved.*
- *Note: staff logs fall under Art. 4 of the Italian Workers' Statute (RC-010).*
