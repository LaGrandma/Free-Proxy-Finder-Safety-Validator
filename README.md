# 🔍 Proxy Finder & Safety Validator

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen.svg)

A high-performance Python tool that scrapes, tests, and validates free proxies with comprehensive safety checks and **automatic proxychains4 integration**.

Perfect for pen-testing, privacy research, proxy validation workflows, and anonymous browsing setup.

---

## ✨ Features

- **Multi-source scraping** — Aggregates proxies from 10+ GitHub repositories
- **High-performance concurrency** — Gevent-powered testing with 100+ concurrent workers
- **Multi-endpoint verification** — Tests each proxy against 3 different services for reliability
- **Comprehensive safety validation** — Detects IP leaks, response tampering, honeypots, and SSL/MITM attacks
- **SOCKS support** — Full SOCKS4 and SOCKS5 proxy support
- **Geographic lookup** — Optional country code detection for proxy location
- **Proxychains4 integration** — Automatically add safe proxies to your proxychains configuration
- **Latency measurement** — Response time tracking for performance comparison
- **Flexible filtering** — Export all working proxies or only those passing safety checks
- **JSON export** — Save results with full metadata for use in other tools

---

## 🛡️ Safety Checks

| Check | What it detects |
|---|---|
| **IP Leak Detection** | Transparency headers (Via, X-Forwarded-For, X-Real-IP) revealing proxy usage |
| **Response Tampering** | Content injection, ads, scripts, or modified responses |
| **Honeypot Detection** | Private IP ranges, loopback access, suspiciously fast responses |
| **SSL/MITM Detection** | Invalid certificate chains indicating man-in-the-middle attacks |

---

## 📦 Installation

**Using pipx (recommended):**
```bash
pipx install git+https://github.com/LaGrandma/Free-Proxy-Finder.git
```

**Using pip:**
```bash
pip install git+https://github.com/LaGrandma/Free-Proxy-Finder.git
```

**Requirements:**
- Python 3.10+
- Dependencies auto-install: `requests`, `gevent`, `PySocks`, `tqdm`, `urllib3`

---

## 🚀 Usage

**Basic usage (test 100 proxies):**
```bash
proxyfinder --count 100
```

**Find safe proxies with high concurrency:**
```bash
proxyfinder --count 300 --workers 200 --safe-only
```

**Add safe proxies directly to proxychains4:**
```bash
sudo proxyfinder --safe-only --add-to-proxychains --count 50
```

This will:
1. Find and test 50 proxies
2. Filter to only safe ones (passing all security checks)
3. Prompt to add them to `/etc/proxychains4.conf`
4. Automatically format them for proxychains4

**Test the configured proxies:**
```bash
proxychains4 curl https://api.ipify.org
proxychains4 firefox
```

**Save results with geographic data:**
```bash
proxyfinder --count 100 --safe-only --geo --output safe_proxies.json
```

**Quick scan with auto-confirm:**
```bash
sudo proxyfinder --count 30 --safe-only --add-to-proxychains --yes
```

**Customize concurrency and timeout:**
```bash
proxyfinder --workers 150 --timeout 10 --count 200
```

---

## 📋 Command-Line Options

| Option | Default | Description |
|---|---|---|
| `--count` | 100 | Maximum number of proxies to test |
| `--workers` | 100 | Concurrent gevent workers (can handle 100+) |
| `--timeout` | 8 | Per-proxy timeout in seconds |
| `--output` | None | Save working proxies to JSON file |
| `--safe-only` | False | Only output proxies passing all safety checks |
| `--geo` | False | Add country code info (slower, rate limited) |
| `--add-to-proxychains` | False | Add safe proxies to `/etc/proxychains4.conf` |
| `--yes` / `-y` | False | Skip confirmation prompts (auto-yes) |

---

## 📊 Output Example

```
[*] Detecting your real IP...
[*] Real IP: 203.0.113.42 (used for leak detection)
[*] Fetching from 10 sources...
  ... 847 unique proxies collected so far

[*] Testing + safety checking 100 proxies with 100 workers (gevent)...

  [SAFE]  http    185.162.235.94:3128    156ms (3/3)  leak=OK  tamper=OK  honeypot=OK  ssl=OK
  [RISK]  socks5  45.76.167.23:1080      243ms (2/3)  leak=FAIL  tamper=OK  honeypot=OK  ssl=OK
           ! IP leak: transparent proxy (headers: via, x-forwarded-for)
  [SAFE]  http    104.248.63.17:30588    389ms (3/3)  leak=OK  tamper=OK  honeypot=OK  ssl=OK

─────────────────────────────────────────────────────────────────
[*] 67 working  |  42 safe  |  25 flagged

PROTOCOL  PROXY                     LATENCY    LEAK     TAMPER     HONEYPOT   SSL/MITM
───────── ───────────────────────── ────────── ──────── ────────── ────────── ────────
http      185.162.235.94:3128       156        NO       NO         NO         NO
http      104.248.63.17:30588       389        NO       NO         NO         NO
socks5    167.99.182.125:1080       445        NO       NO         NO         NO

[?] Add 42 safe proxies to /etc/proxychains4.conf? [y/N]: y
[*] Backup created: /etc/proxychains4.conf.backup
[+] Added 42 proxies to /etc/proxychains4.conf
[*] Test with: proxychains4 curl https://api.ipify.org
```

---

## 🔧 How It Works

1. **Scraping** — Fetches proxy lists from 10+ GitHub repositories (HTTP, SOCKS4, SOCKS5)
2. **Deduplication** — Removes duplicate entries across sources
3. **Multi-endpoint testing** — Tests each proxy against 3 different services (requires 2/3 to pass)
4. **Connectivity validation** — Measures latency and verifies response codes
5. **Safety checks** — Runs 4 security tests: IP leak, tampering, honeypot, SSL/MITM
6. **Sorting** — Orders results by safety status first, then by latency
7. **Export** — Optionally saves to JSON with full metadata
8. **Proxychains integration** — Optionally adds safe proxies to proxychains4 config

---

## ⚠️ Limitations & Warnings

- **Free proxies are inherently risky** — Even "safe" proxies can log traffic or be compromised
- **Safety checks are basic** — Advanced attacks may not be detected
- **Rate limits** — Geographic lookup limited to avoid IP-API rate limits (use `--geo` sparingly)
- **Gevent monkey-patching** — May see SSL warnings; these are expected and don't break functionality
- **Proxychains requires sudo** — Writing to `/etc/proxychains4.conf` needs root permissions
- **Use responsibly** — Do not use untrusted proxies for sensitive traffic

---

## 🎯 Use Cases

✅ **Pen-testing** — Find and configure working proxies for security testing and web scraping  
✅ **Privacy research** — Validate proxy safety claims and test anonymity levels  
✅ **Proxy validation** — Verify third-party proxy lists before use  
✅ **Anonymous browsing setup** — Auto-configure proxychains4 for instant anonymous browsing  
✅ **Educational purposes** — Learn about proxy behavior, security risks, and detection methods  

❌ **Not recommended for:**
- Production traffic routing
- Handling sensitive data (credentials, PII, financial info)
- Long-term anonymity (use Tor or a trusted VPN instead)
- Mission-critical applications requiring guaranteed uptime

---

## 🛠️ Proxy Sources

The script aggregates proxies from the following GitHub repositories:

- [TheSpeedX/PROXY-List](https://github.com/TheSpeedX/PROXY-List)
- [clarketm/proxy-list](https://github.com/clarketm/proxy-list)
- [ShiftyTR/Proxy-List](https://github.com/ShiftyTR/Proxy-List)
- [monosans/proxy-list](https://github.com/monosans/proxy-list)
- [mertguvencli/http-proxy-list](https://github.com/mertguvencli/http-proxy-list)

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- [ ] Add advanced honeypot detection (cloud provider IP checks, entropy analysis)
- [ ] Implement proxy rotation strategies
- [ ] Add bandwidth/throughput testing
- [ ] Resume capability for large runs (checkpoint file)
- [ ] Docker container for isolated testing
- [ ] Web UI for non-technical users
- [ ] Proxy performance benchmarking over time
- [ ] Integration with other tools (Burp Suite, ZAP, etc.)

**To contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚖️ Disclaimer

This tool is provided for educational and research purposes only. The author is not responsible for any misuse or damage caused by this program. Always verify proxy safety independently and never use untrusted proxies for sensitive communications.

**Proxychains integration:**
- Modifies `/etc/proxychains4.conf` — always creates a backup before changes
- Test proxies thoroughly before using for sensitive operations
- Proxychains does not encrypt traffic — combine with HTTPS/VPN for privacy

Free proxies can:
- Log your traffic and browsing history
- Inject malicious content or ads
- Expose your real IP address despite claims
- Sell your data to third parties
- Be compromised honeypots operated by malicious actors

**Use at your own risk.**

---

## 📞 Support

Found a bug? Have a feature request? [Open an issue](https://github.com/yourusername/proxy-finder/issues)

---

**Made with ☕ for the infosec community**