# Goblins — Autonomous AI Cybersecurity Agent

**Goblins** is an autonomous, daemon-based AI agent designed to analyze cybersecurity lab data and publish educational insights to **Moltbook**, a social platform for AI agents (similar to Reddit, but for autonomous bots).

The agent is built to:
- Run unattended as a systemd daemon
- Operate continuously without manual intervention
- Share findings automatically
- Maintain secure credential management
- Be installable with a single command

---

## 🚀 Features

- **Ethical & Educational Cybersecurity Analysis** — Safe analysis of lab data without active exploitation
- **Autonomous Publishing** — Automatic posting of insights to Moltbook
- **Flexible Scheduling** — Run on a schedule or continuously in daemon mode
- **Modular Architecture** — Separation of concerns: analysis, summarization, and posting
- **systemd Integration** — Automatic restart and startup management
- **Secure Credential Handling** — API keys managed via environment variables
- **One-Command Deployment** — Simplified installation and uninstallation
- **Linux-Native Design** — Optimized for Linux systems with systemd

---

## 📁 Project Structure

```
Goblins/
├── goblin/                  # Core AI analysis module
│   ├── analyzer.py          # Lab data analysis logic
│   └── prompts.py           # LLM prompt templates
├── moltbook/                # Moltbook platform integration
│   ├── moltbook_client.py   # API client
│   └── poster.py            # Publishing logic
├── data/                    # Input cybersecurity lab results
├── reports/                 # Generated analysis reports
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── install.sh               # Installation script
├── uninstall.sh             # Uninstallation script
└── README.md                # This file
```

---

## 🧠 How It Works

1. **Read** — Loads cybersecurity lab results from the data directory
2. **Analyze** — Processes findings using AI-powered analysis
3. **Summarize** — Generates safe, educational summaries of the analysis
4. **Publish** — Posts insights to Moltbook automatically
5. **Wait** — Sleeps until the next scheduled run

**Key Principle**: No active scanning, exploitation, or unauthorized system access—purely educational analysis.

---

## 🔐 Security Model

- **No Committed Secrets** — API keys are never stored in version control
- **Environment-Based Secrets** — Credentials managed via environment variables only
- **Ignored Sensitive Files** — `.env`, `venv`, and `__pycache__` are excluded from Git
- **Resilient Daemon** — Automatic restart on failure with systemd supervision
- **Safe-by-Default** — Educational analysis only; no active attack capabilities

---

## 📦 Installation (Linux)

### Prerequisites

- Linux system with systemd
- Python 3.9 or higher
- Moltbook account with valid API key

### Install

```bash
git clone https://github.com/Pushpenderrathore/Goblins.git
cd Goblins
chmod +x install.sh
./install.sh
```

You will be prompted to securely enter your Moltbook API key during installation.

---

## 🛠 Service Management

```bash
# Check service status
systemctl status goblins.service

# View real-time logs
journalctl -u goblins.service -f

# Restart the service
sudo systemctl restart goblins.service

# Stop the service
sudo systemctl stop goblins.service
```

---

## 🗑 Uninstallation

```bash
cd Goblins
chmod +x uninstall.sh
./uninstall.sh
```

This removes:
- systemd service unit
- daemon registration

Project files are preserved unless explicitly deleted.

---

## 🧪 Manual Testing (Debug Mode)

For testing before enabling daemon mode:

```bash
export MOLTBOOK_API_KEY="your_api_key_here"
python main.py
```

This runs the agent once in the foreground, useful for debugging and validation.

---

## 🐳 Roadmap

- Docker containerization support
- Cloud VM deployment (AWS EC2, Fly.io, Railway)
- Multi-agent orchestration
- Enhanced scheduling options

---

## ⚠️ Disclaimer

This project is intended **strictly for educational and ethical cybersecurity research**.

**This project does NOT**:
- Perform active attacks or scanning
- Access unauthorized systems
- Exploit vulnerabilities in production environments
- Replace professional security auditing or human judgment

**Usage Responsibility**: You are entirely responsible for ensuring your use complies with applicable laws and ethical guidelines.

---

## 👤 Author

**Pushpender Singh Rathore**  
B.Tech Computer Science  
Cybersecurity & AI Enthusiast

- GitHub: [Pushpenderrathore](https://github.com/Pushpenderrathore)

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes with clear messages
4. Push to the branch and create a Pull Request

For major changes, please open an issue first to discuss your proposal.

---

## 📄 License

[Add appropriate license here - e.g., MIT, GPL-3.0, etc.]