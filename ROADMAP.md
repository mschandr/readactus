# Readactus Roadmap

This document outlines planned features and priorities for upcoming versions of **Readactus**.
Timelines are tentative and subject to change.

---

## 🎯 Near-Term (v1.x)
Focus: solid core experience, freemium enforcement, and usability polish.

- [x] Basic GUI (tkinter) with config save/load
- [x] Encrypted config using `cryptography.Fernet`
- [x] MySQL connection testing
- [ ] Enforce freemium licensing model (200 MB free limit in binaries)
- [ ] Release pre-built binaries for Windows, macOS, and Linux
- [ ] Improve obfuscation library (names, emails, phone numbers, addresses)
- [ ] Add saved obfuscation profiles (Single DB license feature)

---

## 🚀 Mid-Term (v2.x)
Focus: performance and user experience.

- [ ] Migrate GUI from tkinter → Dear PyGui
- [ ] Multi-threaded obfuscation for larger datasets
- [ ] CLI mode for automation (Single DB and Multi-DB licenses)
- [ ] Multi-DB support with shared rulesets (Multi-DB license feature)
- [ ] Custom rule sets & schema pattern matching (Multi-DB license feature)
- [ ] Export/import obfuscation profiles for team sharing

---

## 🌐 Long-Term (v3.x and Beyond)
Focus: enterprise readiness, integrations, and advanced features.

- [ ] Scheduling (nightly/weekly redactions)
- [ ] API mode for pipeline/test automation
- [ ] Pre-built industry libraries (e.g., healthcare, financial, legal compliance)
- [ ] Enterprise support packages (priority SLAs, custom features)
- [ ] Expanded database support (PostgreSQL, SQL Server, Oracle, SQLite)
- [ ] Cloud integration for obfuscation jobs (optional SaaS offering)

---

## 📌 Notes
- The **MIT-licensed source code** will continue to evolve in parallel with the **commercial binaries**.
- New premium features (multi-DB, custom rule sets, compliance libraries) will be added first to the **commercial binaries**.
- Community contributions are welc

