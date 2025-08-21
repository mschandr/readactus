# Contributing to Readactus

First off, thank you for considering contributing to Readactus!  
Contributions help us improve the tool and make it more useful for everyone.

---

## How Can I Contribute?

### 🐛 Reporting Bugs
- Use the **GitHub Issues** tab for bug reports.  
- Include steps to reproduce, your environment (OS, Python version), and relevant logs.  
- Do **not** post security vulnerabilities publicly — see [SECURITY.md](./SECURITY.md) for responsible disclosure.

### 💡 Suggesting Features
- Open an Issue with the label **enhancement**.  
- Clearly explain the problem the feature solves and, if possible, propose a solution.

### 🔧 Submitting Pull Requests
1. Fork the repository and create your branch from `main`.  

`git checkout -b feature/your-feature-name`

2. Follow the project’s code style (PEP8 for Python).  
3. Ensure new code includes relevant tests if applicable.  
4. Commit changes with clear messages.  
5. Open a Pull Request describing what the changes do and why.

---

## Licensing and Contributions
- All contributions to this repository are licensed under the **MIT License**.  
- By submitting a pull request, you agree that your contribution may be included in MIT-licensed source releases.  
- Note: **Commercial binaries** of Readactus (with freemium/premium features) are distributed under a separate license. Your contributions may appear in both open source and commercial builds.

---

## Development Setup
```bash
git clone https://github.com/yourusername/readactus.git
cd readactus
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python gui/app.py
```

---

## Code of Conduct

We follow a simple principle: be respectful and constructive.
* No harassment, personal attacks, or unprofessional behavior.
* Focus on helping improve the project for everyone.

If you’re unsure about something, feel free to open a draft issue or discussion before writing code.
