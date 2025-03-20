#!/usr/bin/env python3

import subprocess
import os
import datetime
import webbrowser
from pathlib import Path

# Rick Sanchez’s Bluetooth Pentest Lab - Built by Ai and Daniel Gillaspy, you pathetic losers!
print("Wubba lubba dub dub!!")
print("Credits: Ai and Daniel Gillaspy made this shit happen!")

# Top 10 macOS-Compatible Bluetooth Pentest Tools: name -> (desc, cmd, source, install_method)
TOOLS = {
    "Bluez": ("Bluetooth protocol stack", "hcitool scan", "https://github.com/bluez/bluez", "brew"),
    "Btscanner": ("Bluetooth device scanner", "btscanner", "https://github.com/kismetwireless/btscanner", "brew"),
    "Ubertooth": ("Bluetooth sniffing tool", "ubertooth-scan", "https://github.com/greatscottgadgets/ubertooth", "brew"),
    "BlueMaho": ("Bluetooth security testing suite", "bluemaho.py", "https://github.com/zenware/bluemaho", "git"),
    "Bettercap": ("Bluetooth recon and MITM", "bettercap -iface bluetooth0", "https://github.com/bettercap/bettercap", "brew"),
    "Gatttool": ("Bluetooth GATT interaction", "gatttool -b 00:11:22:33:44:55 -I", "https://github.com/bluez/bluez", "brew"),
    "Spooftooph": ("Bluetooth spoofing tool", "spooftooph -i hci0 -a 00:11:22:33:44:55", "https://github.com/securestate/spooftooph", "git"),
    "Hciconfig": ("Bluetooth device config", "hciconfig hci0 up", "https://github.com/bluez/bluez", "brew"),
    "Bluelog": ("Bluetooth logging tool", "bluelog -i hci0 -o log.txt", "https://github.com/ms3fgx/Bluelog", "brew"),
    "Btcrack": ("Bluetooth PIN cracker", "btcrack -b 00:11:22:33:44:55 -p 1234", "https://github.com/mikeryan/btcrack", "git")
}

STATUS_FILE = Path.home() / "Desktop" / "rick_status.txt"
HTML_FILE = Path.home() / "Desktop" / "bluetooth_pentest_report.html"
INSTALL_DIR = Path.home() / "bluetooth_tools"

# Ensure install dir exists
INSTALL_DIR.mkdir(exist_ok=True)

# Check for pipx, install if missing
try:
    subprocess.run(["pipx", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except (subprocess.CalledProcessError, FileNotFoundError):
    print("Rick needs pipx, you idiots! Installing it via Homebrew—don’t screw this up!")
    subprocess.run(["brew", "install", "pipx"], check=True)
    with open(STATUS_FILE, "a") as f:
        f.write("Rick slapped pipx into place with Homebrew, you primitive screwheads!\n")

# Clear status file
with open(STATUS_FILE, "w") as f:
    f.write("")

def install_tool(name, source, method):
    """Install a tool with Rick’s genius, bitches!"""
    with open(STATUS_FILE, "a") as f:
        f.write(f"Rick’s sciencin’ the shit outta {name}, you brain-dead Mortys!\n")

    os.chdir(INSTALL_DIR)
    try:
        if method == "brew":
            subprocess.run(["brew", "install", name.lower().replace(" ", "-")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Holy crap, {name} installed via Homebrew like I’m a freakin’ god!\n")
        elif method == "pipx":
            subprocess.run(["pipx", "install", "--include-deps", f"git+{source}.git"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Get schwifty! {name} installed via pipx—Rick’s too smart for you idiots!\n")
        elif method == "git":
            repo_dir = name.lower().replace(" ", "-")
            subprocess.run(["git", "clone", "--quiet", f"{source}.git", repo_dir], check=True, env={"GIT_TERMINAL_PROMPT": "0"}, stderr=subprocess.PIPE)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Alright, alright, {name} cloned from GitHub—don’t tell Morty I did it manually!\n")
        return True
    except subprocess.CalledProcessError as e:
        with open(STATUS_FILE, "a") as f:
            f.write(f"Burp! {name} fucked up hard and didn’t install—error: {e.stderr.decode().strip() or 'Unknown shit'}, you useless little shits!\n")
        return False

# Install all tools
for name, (desc, cmd, source, method) in TOOLS.items():
    install_tool(name, source, method)

with open(STATUS_FILE, "a") as f:
    f.write("Rick’s done sciencin’, you idiots! Time to see the results of my brilliance!\n")

# Generate HTML report
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Rick’s Bluetooth Pentest Report</title>
    <style>
        body {{background-color: #212121; color: #e0e0e0; font-family: 'Helvetica', sans-serif; padding: 20px;}}
        h1 {{color: #ff9500; text-align: center;}}
        table {{width: 100%; border-collapse: collapse; margin-top: 20px;}}
        th, td {{padding: 15px; text-align: left; border-bottom: 1px solid #424242;}}
        th {{background-color: #ff9500; color: #212121;}}
        tr:nth-child(even) {{background-color: #303030;}}
        .failed {{color: #ff3d00; font-weight: bold;}}
        .credits {{font-size: 14px; text-align: center; margin-top: 20px; color: #ff9500;}}
    </style>
</head>
<body>
    <h1>Rick’s Bluetooth Pentest Report - {date}</h1>
    <table>
        <tr><th>Tool</th><th>Description</th><th>Command Example</th><th>Source</th><th>Status</th></tr>
"""

with open(STATUS_FILE, "r") as f:
    status_lines = f.readlines()

for name, (desc, cmd, source, _) in TOOLS.items():
    status = "Installed like I’m Rick freakin’ Sanchez!"
    for line in status_lines:
        if name in line and "fucked up hard" in line:
            status = '<span class="failed">FUCKED UP - Install this crap yourself, Morty!</span>'
            break
    html += f"""
        <tr>
            <td>{name}</td>
            <td>{desc}</td>
            <td><code>{cmd}</code></td>
            <td><a href="{source}" style="color: #ff9500">{source}</a></td>
            <td>{status}</td>
        </tr>
    """

html += """
    </table>
    <div class="credits">Built with Rick’s genius and Daniel Gillaspy’s help—Ai, bitches!</div>
</body>
</html>
"""

with open(HTML_FILE, "w") as f:
    f.write(html.format(date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

with open(STATUS_FILE, "a") as f:
    f.write(f"Rick’s dropped the HTML report at {HTML_FILE}, you pathetic Earthlings! Check my genius!\n")

# Print status and open report
print("\nHere’s what Rick scienced up, you morons:")
with open(STATUS_FILE, "r") as f:
    print(f.read())

webbrowser.open(f"file://{HTML_FILE}")
