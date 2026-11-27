<p align="center"><img src="https://raw.githubusercontent.com/EduWISP/.github/main/branding/eduwisp-mark.svg" alt="EduWISP" height="72"></p>

# eduwisp-audit

**Audit e reporting** · *Audit & Reporting*

Registro non alterabile delle operazioni amministrative e report minimizzati.

> 🧪 **Stato: prototipo v0.** Registro in sola aggiunta (`AuditEvent`) con la funzione `record()`; usato dal «vedi come» dell'amministratore ([ADR-0018](https://eduwisp.org/docs/decisioni/0018-interfaccia-per-ruoli/)). La progettazione è nella [documentazione EduWISP](https://eduwisp.org/docs/sicurezza-privacy/sicurezza/).

🇬🇧 *Tamper-resistant log of administrative operations and minimised reports. **Status: prototype v0**: append-only `AuditEvent` with `record()`. See the [design docs](https://eduwisp.org/docs/en/security-privacy/security/).*

## Documentazione / Documentation

- Progettazione / Design: <https://eduwisp.org/docs/sicurezza-privacy/sicurezza/>
- Mappa dei repository / Repository map: <https://eduwisp.org/docs/architettura/repository/>
- Documentazione del modulo / Module docs: [`docs/user/`](docs/user/) · [`docs/developer/`](docs/developer/)

## Dipendenze / Dependencies

[`eduwisp-users`](https://github.com/EduWISP/eduwisp-users)

## Uso / Usage

```python
from eduwisp_audit.log import record
from eduwisp_audit.models import Action

record(Action.VIEW_AS_START, actor=request.user, organization=scuola, subject=docente,
       reason="richiesta di assistenza", role="teacher")
```

Gli eventi non si modificano e non si cancellano dall'applicazione; nell'amministrazione li vedono solo gli amministratori di sistema, in sola lettura.

## Privacy

Dati personali previsti e regole: [PRIVACY.md](PRIVACY.md). Il rispetto della normativa su privacy e minori è un vincolo bloccante ([ADR-0008](https://eduwisp.org/docs/decisioni/0008-conformita-normativa/)).

## Responsabile del modulo / Module owner

Cerchiamo persone che vogliano prendere in carico questo modulo! Proponiti in [Discussions](https://github.com/EduWISP/docs/discussions). / *Want to own this module? Say hi in Discussions.*

## Contribuire / Contributing

Vedi [CONTRIBUTING](https://github.com/EduWISP/.github/blob/main/CONTRIBUTING.md) e il [Codice di condotta](https://github.com/EduWISP/.github/blob/main/CODE_OF_CONDUCT.md). **Mai dati personali reali** di studenti, famiglie o personale.

## Licenza / License

**AGPL-3.0-or-later**, con termini aggiuntivi di attribuzione e tutela del nome (sezione 7): vedi [LICENSE](LICENSE) e [NOTICE.md](NOTICE.md). Chi usa o modifica EduWISP deve sempre indicare «Basato su EduWISP» e non può usare il nome e il logo per versioni modificate. Licenza scelta secondo le [linee guida AgID](https://eduwisp.org/docs/decisioni/0006-licenza/) per il software usato via rete.

*AGPL-3.0-or-later with additional attribution and trademark terms (section 7): see LICENSE and NOTICE.md.*

I contributi richiedono il [DCO](https://github.com/EduWISP/.github/blob/main/CONTRIBUTING.md#dco) (`git commit -s`).
