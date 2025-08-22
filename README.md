# Readactus

**Readactus** is a desktop tool for safely replicating production MySQL databases to local developer environments by obfuscating sensitive data such as passwords, emails, and IDs. Designed for highly regulated industries where data privacy is non-negotiable.

Run production-like tests without risking compliance breaches.

---

## 🚀 Features

- Obfuscates sensitive MySQL database content for dev/test use
- Connects to source (remote) and target (local) MySQL databases
- Passwords encrypted at rest using `cryptography.Fernet`
- Simple GUI built with `tkinter` (Dear PyGui coming soon)
- Secure config file with masked password storage
- Connection testing built-in

---

## 💰 Pricing & Licensing

Readactus uses a **freemium licensing model**:

| Plan | Free Tier | Single DB License | Multi-DB License |
|------|-----------|-------------------|------------------|
| **Price** | $0 | $500 (one-time) | $1,000 (one-time) |
| **Data Size** | Up to 200 MB | Unlimited | Unlimited |
| **Databases** | 1 database | 1 database | Multiple databases |
| **Obfuscation** | ✅ | ✅ | ✅ |
| **Saved Profiles** | ❌ | ✅ | ✅ |
| **CLI Mode** | ❌ | ✅ | ✅ |
| **Custom Rule Sets** | ❌ | ❌ | ✅ |
| **Support** | Community | Email | Priority |
| **License** | MIT (source code) | Commercial (binary) | Commercial (binary) |

- The **source code** in this repository is MIT licensed.
- **Pre-built binaries** (with usage limits and premium features) are distributed under a separate commercial license. See [COMMERCIAL_LICENSE.md](./COMMERCIAL_LICENSE.md).

---

## 🛠 Requirements

- Python 3.10+
- `cryptography`
- `mysql-connector-python`

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📦 Installation
```bash
git clone https://github.com/yourusername/readactus.git
cd readactus
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python gui/app.py
```

## 🔒 Security

* Config file (`readactus_config.json`) contains encrypted passwords.
* Encryption key is stored locally in `readactus.key`.
* These files **must not** be committed to source control.

Always ensure .gitignore includes:

```
.venv/
__pycache__/
readactus.key
readactus_config.json
```

See SECURITY.md for details on responsible disclosure.

🧭 Roadmap

* v1.x → Tkinter GUI, freemium limits (200 MB free, unlimited paid).
* v2.x → Migration to Dear PyGui for a modern UI, performance optimizations.
* Future → Multi-DB rule sets, scheduling, API integrations, compliance libraries.
* Further into the future, multiple DBs eventually Postgres, then Oracle, then MS SQL (at some point I hope to make enough money that I can actually pay for licenses of both Oracle and MS SQL)


## 🧪 Status
Version 0.1 — Basic GUI, config save/load, encrypted secrets, and DB connection validation are functional.

## ✨ Powered by Damian
This tool is part of the broader Daemon tool family.

This repository is open source under MIT. Pre-built binaries with freemium and premium features are distributed under a separate commercial license. See COMMERCIAL_LICENSE.md
