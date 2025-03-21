# osxBLUETOOTH
Here’s a professional README.md file for your Bluetooth Pentest Lab script. It tones down the Rick Sanchez humor to a subtle nod, maintains a clean and structured layout, and includes all necessary details like tools, commands, and installation instructions in a polished, professional manner.

Bluetooth Pentest Lab
The Bluetooth Pentest Lab is a Python-based automation script designed to streamline the installation and management of Bluetooth penetration testing tools on macOS systems. Developed by Daniel Gillaspy with AI assistance, this project simplifies the setup process for security researchers and pentesters by installing a curated list of tools, tracking their installation status, and generating a detailed HTML report.
Overview
This script installs a collection of macOS-compatible Bluetooth pentesting tools using Homebrew, pipx, or Git, depending on the tool’s requirements. It creates a status log (~/Desktop/rick_status.txt) and an HTML report (~/Desktop/bluetooth_pentest_report.html) summarizing the installation process, which is automatically opened in your browser upon completion.
Supported Tools
The following table lists the tools included in this lab, along with their descriptions and example commands:
Tool
Description
Example Command
Bluez
Bluetooth protocol stack
hcitool scan
Btscanner
Bluetooth device scanner
btscanner
Ubertooth
Bluetooth sniffing tool
ubertooth-scan
BlueMaho
Bluetooth security testing suite
bluemaho.py
Bettercap
Bluetooth recon and MITM
bettercap -iface bluetooth0
Gatttool
Bluetooth GATT interaction
gatttool -b 00:11:22:33:44:55 -I
Spooftooph
Bluetooth spoofing tool
spooftooph -i hci0 -a 00:11:22:33:44:55
Hciconfig
Bluetooth device configuration
hciconfig hci0 up
Bluelog
Bluetooth logging tool
bluelog -i hci0 -o log.txt
Btcrack
Bluetooth PIN cracker
btcrack -b 00:11:22:33:44:55 -p 1234
Prerequisites
Before running the script, ensure the following dependencies are installed:
	•	Python 3: Required to execute the script.
	•	Homebrew: Package manager for macOS (used for most tool installations).
	•	pipx: Python package installer (automatically installed if missing).
	•	Git: For cloning repositories where necessary.
To install Homebrew and Git on macOS, run:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
Installation
	1	Download the Script: Clone or download this repository to your local machine.
	2	Run the Script: Execute the script using Python 3: python3 bluetooth_pentest_lab.py
	3	
	4	Review Output: The script will:
	◦	Install the tools into ~/bluetooth_tools.
	◦	Log progress to ~/Desktop/rick_status.txt.
	◦	Generate and open an HTML report at ~/Desktop/bluetooth_pentest_report.html.
How It Works
	•	Dependency Check: Verifies pipx is installed, installing it via Homebrew if absent.
	•	Tool Installation: Installs each tool using the specified method (Homebrew, pipx, or Git cloning).
	•	Status Tracking: Logs installation success or failure to a text file.
	•	Report Generation: Creates an HTML report with tool details, example commands, sources, and installation status.
Output
Upon completion, the script outputs:
	•	A status log (~/Desktop/rick_status.txt) detailing the installation process.
	•	An HTML report (~/Desktop/bluetooth_pentest_report.html) opened in your default browser, summarizing tool installation results.
Credits
	•	Daniel Gillaspy: Lead developer.
	•	AI Assistance: Supporting development and optimization.
Developed on March 20, 2025, with a nod to the chaotic genius of Rick Sanchez.
License
This project is released under the MIT License. See the LICENSE file for details.

This version is professional, concise, and suitable for a GitHub repository or a formal project presentation. It keeps the table of tools with sample commands and descriptions, provides clear instructions, and maintains a subtle Rick Sanchez reference in the credits for personality. Let me know if you’d like adjustments!
