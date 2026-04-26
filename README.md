# Linux-cli-assistant
A lightweight AI CLI agent for Termux+Proot Debian that translates natural language into Linux commands. 
🤖 AI Terminal Agent (Termux + Debian)

A simple AI-powered command-line assistant that converts natural language into Linux commands and executes them safely.

---

🚀 Features

- 🧠 Convert English → Linux commands
- 💻 Works inside Termux + Proot Debian
- 🖥️ Compatible with VNC GUI terminal
- ⚠️ Confirmation before execution (safe mode)
- 📂 Supports file & folder operations

---

🧱 Requirements

- Android device
- Termux installed
- Proot Debian installed inside Termux
- Internet connection (for API)

---

⚙️ Setup Guide

1️⃣ Open Termux and enter Debian

proot-distro login debian

---

2️⃣ Update system

apt update && apt upgrade -y

---

3️⃣ Install Python

apt install python3 python3-pip python3-venv -y

---

4️⃣ Create virtual environment

python3 -m venv myenv

Activate it:

source myenv/bin/activate

---

5️⃣ Install dependencies

pip install requests

---

6️⃣ Create agent file

nano agent.py

Paste your Python code inside and save.

---

7️⃣ Add API key (secure method)

In terminal:

export OPENROUTER_API_KEY="your_api_key_here"

In Python file:

import os
API_KEY = os.getenv("OPENROUTER_API_KEY")

---

8️⃣ Run the agent

python agent.py

---

🧪 Usage

Type commands in natural language:

/root $ create folder test
AI suggests: mkdir test
Run this command? (y/n): y

---
https://github.com/user-attachments/assets/8fc8e09d-2d18-4dfc-967a-6420a4580d12

---
📁 Navigation Example

go inside folder test
list files
show current directory

---

⚠️ Safety Warning

- Always review commands before running
- Do NOT execute unknown or dangerous commands
- Avoid commands like "rm -rf /"

---

🖥️ GUI Mode (Optional)

You can run this inside VNC GUI:

- Open terminal inside VNC
- Activate environment
- Run:

python agent.py

---

🧠 How It Works

User Input → AI API → Linux Command → Execution

---

🔒 Security Note

- Never expose your API key publicly
- Use environment variables instead of hardcoding

---

🚧 Limitations

- No memory (single command only)
- No GUI automation
- Depends on API availability

---

🚀 Future Improvements

- Command history
- Safety filter for dangerous commands
- Multi-step task execution
- GUI automation support

---

📜 License

This project is for learning and experimentation purposes.

---

🙌 Author

Built by a learner exploring AI + Linux automation.
