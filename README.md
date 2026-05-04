# 🔍 Proxy Finder & Safety Validator
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen.svg)


A multi-threaded Python tool that scrapes, tests, and validates free proxies from multiple sources with built-in security checks.

Perfect for pen-testing, privacy research, and proxy validation workflows.

---

## ✨ Features

- **Multi-source scraping** — Aggregates proxies from 10+ GitHub repositories
- **Concurrent testing** — Multi-threaded validation with configurable worker count
- **Safety validation** — Detects IP leaks, response tampering, and honeypot characteristics
- **Latency measurement** — Response time tracking for performance comparison
- **Flexible filtering** — Export all working proxies or only those passing safety checks
- **Easy output** — Save results to file for use in other tools

---

## 🛡️ Safety Checks

| Check | What it detects |
|---|---|
| **IP Leak Detection** | X-Forwarded-For, Via, X-Real-IP headers exposing your real IP |
| **Response Tampering** | Proxies modifying response bodies or injecting content |
| **Honeypot Detection** | Private IP ranges, common honeypot characteristics |

---

## 📦 Installation

**Requirements:**
- Python 3.10+
- `requests` library (auto-installed if missing)

**Clone & run:**
```bash
git clone https://github.com/yourusername/proxy-finder.git
cd proxy-finder
python3 proxy_finder.py
```

The script will automatically install `requests` if it's not already present.

---

## 🚀 Usage

**Basic usage (test 100 proxies):**
```bash
python3 proxy_finder.py
```

**Test more proxies:**
```bash
python3 proxy_finder.py --count 300
```

**Save working proxies to file:**
```bash
python3 proxy_finder.py --output proxies.txt
```

**Only save proxies that pass all safety checks:**
```bash
python3 proxy_finder.py --safe-only --output safe_proxies.txt
```

**Customize concurrency and timeout:**
```bash
python3 proxy_finder.py --threads 50 --timeout 10
```

---

## 📋 Command-Line Options

| Option | Default | Description |
|---|---|---|
| `--count` | 100 | Maximum number of proxies to test |
| `--threads` | 40 | Number of concurrent test threads |
| `--timeout` | 8 | Per-proxy timeout in seconds |
| `--output` | None | Save working proxies to file |
| `--safe-only` | False | Only output proxies passing all safety checks |

---

## 📊 Output Example

```
[*] Detecting your real IP...
[*] Real IP: 203.0.113.42 (used for leak detection)
[*] Fetching from 10 sources...
  ... 847 unique proxies collected so far

[*] Testing + safety checking 100 proxies (40 threads)...

  [SAFE]   185.162.235.94:3128       156ms  leak=OK  tamper=OK  honeypot=OK
  [RISK]   45.76.167.23:8080         243ms  leak=FAIL  tamper=OK  honeypot=OK
           ! IP leak: x-forwarded-for: 203.0.113.42
  [SAFE]   104.248.63.17:30588       389ms  leak=OK  tamper=OK  honeypot=OK

─────────────────────────────────────────────────────────────────
[*] 67 working  |  42 safe  |  25 flagged

PROXY                     LATENCY    LEAK     TAMPER     HONEYPOT
───────────────────────── ────────── ──────── ────────── ────────
185.162.235.94:3128       156        NO       NO         NO
104.248.63.17:30588       389        NO       NO         NO
```

---

## 🔧 How It Works

1. **Scraping** — Fetches proxy lists from multiple GitHub repositories
2. **Deduplication** — Removes duplicate entries across sources
3. **Connectivity test** — Validates each proxy can reach the internet
4. **Safety checks** — Runs IP leak, tampering, and honeypot detection
5. **Sorting** — Orders results by safety status and latency
6. **Export** — Optionally saves working proxies to file

---

## ⚠️ Limitations & Warnings

- **Free proxies are inherently risky** — Even "safe" proxies can log traffic or inject content
- **No SOCKS protocol support** — Currently only tests HTTP/HTTPS proxies (SOCKS proxies in sources will fail)
- **Safety checks are basic** — Advanced MITM attacks may not be detected
- **IP leak check requires internet access** — If your real IP cannot be detected, leak checks are skipped
- **Use responsibly** — Do not use untrusted proxies for sensitive traffic

---

## 🎯 Use Cases

✅ **Pen-testing** — Find working proxies for web scraping and security testing  
✅ **Privacy research** — Validate proxy safety claims  
✅ **Proxy validation** — Verify third-party proxy lists before use  
✅ **Educational purposes** — Learn about proxy behavior and security risks  

❌ **Not recommended for:**
- Production traffic routing
- Handling sensitive data
- Long-term anonymity (use Tor or a trusted VPN instead)

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

- [ ] Add SOCKS4/SOCKS5 protocol support
- [ ] Implement SSL/TLS certificate validation checks
- [ ] Add geographic location detection (IP geolocation)
- [ ] Bandwidth/throughput testing
- [ ] Resume capability for large runs
- [ ] JSON output format with full safety metadata

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

Free proxies can:
- Log your traffic
- Inject malicious content
- Expose your real IP address
- Sell your data to third parties

Use at your own risk.

---

## 📞 Support

Found a bug? Have a feature request? [Open an issue](https://github.com/yourusername/proxy-finder/issues)

---

**Made with ☕ for the infosec community**
