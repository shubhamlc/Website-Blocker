import time
import os
from datetime import datetime

# Path to hosts file (Windows/Linux)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == "nt" else "/etc/hosts"
redirect_ip = "127.0.0.1"
log_file = "web_blocker_log.txt"

# --- UTILITY FUNCTIONS ---

def log_action(action, websites):
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - {action}: {', '.join(websites)}\n")

def normalize(site):
    return site.replace("www.", "").lower()

def get_site_variants(site):
    site = normalize(site)
    return [site, f"www.{site}"]

# --- CORE FUNCTIONALITY ---

def block_websites(websites):
    try:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in websites:
                for variant in get_site_variants(site):
                    if variant not in content:
                        file.write(f"{redirect_ip} {variant}\n")
        log_action("Blocked", websites)
        print(f"Websites blocked: {', '.join(websites)}")
    except PermissionError:
        print("❌ Permission denied! Run the script as administrator.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def unblock_websites(websites):
    try:
        with open(hosts_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(variant in line for site in websites for variant in get_site_variants(site)):
                    file.write(line)
            file.truncate()
        log_action("Unblocked", websites)
        print(f"Websites unblocked: {', '.join(websites)}")
    except Exception as e:
        print(f"❌ Error while unblocking: {e}")

def block_temporarily(websites, minutes):
    block_websites(websites)
    print(f"⏳ Blocked for {minutes} minutes...")
    try:
        time.sleep(minutes * 60)
    except KeyboardInterrupt:
        print("\n⛔ Interrupted. Still unblocking...")
    unblock_websites(websites)

# --- MAIN MENU ---

if __name__ == "__main__":
    print("📵 Website Blocker Pro Max v2")
    sites_to_block = ["facebook.com", "instagram.com"]

    action = input("Choose action - (b)lock / (u)nblock / block (t)emporarily: ").lower().strip()

    if action == 'b':
        block_websites(sites_to_block)
    elif action == 'u':
        unblock_websites(sites_to_block)
    elif action == 't':
        try:
            duration = int(input("Enter duration in minutes: "))
            block_temporarily(sites_to_block, duration)
        except ValueError:
            print("❌ Invalid number.")
    else:
        print("❌ Invalid option selected.")
