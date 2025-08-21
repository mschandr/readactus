# Security Policy

## Supported Versions
Readactus is under active development. Security fixes will be applied to the most recent stable release only.

| Version | Supported |
|---------|------------|
| 0.1.x   | ✅ |
| < 0.1   | ❌ |

---

## Reporting a Vulnerability
If you discover a security vulnerability in Readactus:

1. **Do not open a public GitHub issue.**  
   This may expose sensitive details to other users.

2. **Contact us directly:**  
   `mark [dot] dhas [at] gmail [dot] com`  
   (replace `[dot]` with `.`)

3. Include in your report:
   - A clear description of the vulnerability
   - Steps to reproduce
   - Any potential impact you are aware of

We aim to acknowledge reports within **72 hours** and will provide updates as we investigate.

---

## Data Handling
- Readactus runs **entirely locally** on your machine.  
- Database content and obfuscation results are **never transmitted** to external servers.  
- Configuration files (`readactus_config.json`) are encrypted at rest, and the encryption key (`readactus.key`) is stored locally only.  

---

## Responsible Disclosure
If you follow the process above, we will:
- Work with you to investigate and resolve the issue quickly
- Credit you in release notes (if desired)
- Keep you updated as the fix progresses

---

## Disclaimer
Readactus is provided “as is.” While we take security seriously, no tool is guaranteed to be free of vulnerabilities. Always test in safe environments before deploying to production.

