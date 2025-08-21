# Readactus

**Readactus** is a desktop tool for safely replicating production MySQL databases to local developer environments by obfuscating sensitive data such as passwords, emails, and IDs. Designed for highly regulated industries where data privacy is non-negotiable.

---

## 🚀 Features

- Obfuscates sensitive MySQL database content for dev/test use
- Connects to source (remote) and target (local) MySQL databases
- Passwords encrypted at rest using `cryptography.Fernet`
- Simple GUI built with `tkinter` for ease of use
- Secure config file with masked password storage
- Connection testing built-in

---

## 🛠 Requirements

- Python 3.10+
- `cryptography`
- `mysql-connector-python`

You can install dependencies with:

```bash
pip install -r requirements.txt
```

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
Config file (readactus_config.json) contains encrypted passwords.

Encryption key is stored locally in readactus.key. This should not be committed to source control.

Always ensure .gitignore includes:

```
.venv/
__pycache__/
readactus.key
readactus_config.json
```

## 🧪 Status
Version 0.1 — Basic GUI, config save/load, encrypted secrets, and DB connection validation are functional.

## ✨ Powered by Damian
This tool is part of the broader Daemon tool family.

This repository is open source under MIT. Pre-built binaries with freemium and premium features are distributed under a separate commercial license. See COMMERCIAL_LICENSE.md
