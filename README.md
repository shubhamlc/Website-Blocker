# 🚫 Website Blocker

Tired of getting distracted by social media or time-wasting sites? `Website Blocker` is a simple but powerful Python script that lets you block/unblock websites manually or temporarily — perfect for studying, working, or deep focus mode.

---

## 🔧 Features

- ⛔ Block websites permanently
- ⏳ Temporarily block websites (auto-unblock after a set time)
- 🔓 Unblock manually
- ✍️ Customizable website list
- 💻 Cross-platform: Windows & Linux
- 📜 All actions logged in `web_blocker_log.txt`

---

## 🚀 How to Use

1. Clone this repo or download the Python file.
2. Open terminal **as Administrator** (Windows) or use `sudo` (Linux).
3. Run:

```bash
python block.py
Follow the menu to block/unblock websites.

🛠️ Customize Blocked Websites
Edit this line inside block.py:


sites_to_block = ["facebook.com", "instagram.com"]
🧠 How It Works
The script modifies your system’s hosts file to redirect specified domains to 127.0.0.1, making them unreachable. It works at the system level — not through browser extensions — so it’s tougher to bypass.

⚠️ Admin Access Required
Modifying the hosts file requires admin/root permission:

Windows: Run Python or terminal as Administrator

Linux: Use sudo python block.py

📜 Log File
All actions are recorded in web_blocker_log.txt. Example:

2025-05-09 18:00 - Blocked: facebook.com, instagram.com
2025-05-09 20:00 - Unblocked: facebook.com, instagram.com

🧑‍💻 Created By
Shubham Lamichhane
👉 github.com/shubhamlc
