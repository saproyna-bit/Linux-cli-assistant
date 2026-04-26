## Linux-cli-assistant

A lightweight AI CLI agent for Termux+Proot Debian that translates natural language into Linux commands. 
---
## AI Terminal Agent (Termux + Debian)

A simple AI-powered command-line assistant that converts natural language into Linux commands and executes them safely.

---

## Features

- 🧠 Convert English → Linux commands
- 💻 Works inside Termux + Proot Debian
- ⚠️ Confirmation before execution (safe mode)
- 📂 Supports file & folder operations

---

## Requirements

- Android device
- Termux installed
- Proot Debian installed inside Termux
- Internet connection (for API)

---

## 1️⃣ Open Termux and enter Debian

```bash
proot-distro login debian
```

## 2️⃣ Update system

```bash
apt update && apt upgrade -y
```

## 3️⃣ Install Python

```bash
apt install python3 python3-pip python3-venv -y
```
## 4️⃣ Create virtual environment

```bash
python3 -m venv myenv
```

```bash
source myenv/bin/activate
```
## 6️⃣ Create agent file

```bash
nano agent.py
```
paste agent.py here

## 7️⃣ Add API key

```bash
export OPENROUTER_API_KEY="your_api_key_here"
```

## 8️⃣ Run

```bash
python agent.py
```

---

## Usage

Type commands in natural language:

/root $ create folder test
AI suggests: mkdir test
Run this command? (y/n): y

---
https://github.com/user-attachments/assets/8fc8e09d-2d18-4dfc-967a-6420a4580d12

---

## ⚠️ Safety Warning

- Always review commands before running
- Do NOT execute unknown or dangerous commands
- Avoid commands like "rm -rf /"

---

## 🖥️ GUI Mode (Optional)

You can run this inside VNC GUI:

- open real vnc viewer in computer
- get ip by typing ifconfig command in termux 
- enter ip and port number
- Open terminal inside VNC
- Activate environment
- Run:

python agent.py

---

## How It Works

User Input → AI API → Linux Command → Execution

---

## 🔒 Security Note

- Never expose your API key publicly
- Use environment variables instead of hardcoding

---

## 🚧 Limitations

- No memory (single command only)
- No GUI automation
- Depends on API availability

---

## 🚀 Future Improvements

- Command history
- Safety filter for dangerous  commands
- Multi-step task execution
- GUI automation support

---

This project is for learning and experimentation purposes.

