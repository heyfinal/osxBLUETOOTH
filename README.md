Here's a reformatted version of your `README.md` with a more polished and structured layout:

```markdown
# osxBLUETOOTH

## Bluetooth Pentest Lab

The Bluetooth Pentest Lab is a Python-based automation script designed to streamline the installation and management of Bluetooth penetration testing tools on macOS systems. Developed by Daniel Gillaspy.

### Overview

This script installs a collection of macOS-compatible Bluetooth pentesting tools using Homebrew, pipx, or Git, depending on the tool’s requirements. It creates a status log at `/Desktop/rick_status.txt`.

### Supported Tools

| Tool       | Description                        | Example Command                           | Source    | Install Method |
|------------|------------------------------------|-------------------------------------------|-----------|----------------|
| Bluez      | Bluetooth protocol stack           | `hcitool scan`                            | Bluez     | brew           |
| Btscanner  | Bluetooth device scanner           | `btscanner`                               | Btscanner | brew           |
| Ubertooth  | Bluetooth sniffing tool            | `ubertooth-scan`                          | Ubertooth | brew           |
| BlueMaho   | Bluetooth security testing suite   | `bluemaho.py`                             | BlueMaho  | git            |
| Bettercap  | Bluetooth recon and MITM           | `bettercap -iface bluetooth0`             | Bettercap | brew           |
| Gatttool   | Bluetooth GATT interaction         | `gatttool -b 00:11:22:33:44:55 -I`        | Gatttool  | brew           |
| Spooftooph | Bluetooth spoofing tool            | `spooftooph -i hci0 -a 00:11:22:33:44:55` | Spooftooph| git            |
| Hciconfig  | Bluetooth device configuration     | `hciconfig hci0 up`                       | Hciconfig | brew           |
| Bluelog    | Bluetooth logging tool             | `bluelog -i hci0 -o log.txt`              | Bluelog   | brew           |
| Btcrack    | Bluetooth PIN cracker              | `btcrack -b 00:11:22:33:44:55 -p 1234`    | Btcrack   | git            |

### Prerequisites

Before running the script, ensure the following dependencies are installed:

- **Python 3:** Required to execute the script.
- **Homebrew:** Package manager for macOS (used for most tool installations).
- **pipx:** Python package installer (automatically installed if missing).
- **Git:** For cloning repositories where necessary.

To install Homebrew and Git on macOS, run:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
```

### Installation

1. **Download the Script:** Clone or download this repository to your local machine.
2. **Run the Script:** Execute the script using Python 3:
    ```sh
    python3 osxBLUETOOTH.py
    ```
3. **Review Output:** The script will:
    - Install the tools into `~/bluetooth_tools`.
    - Log progress to `~/Desktop/rick_status.txt`.
    - Generate and open an HTML report at `~/Desktop/bluetooth_pentest_report.html`.

### How It Works

- **Dependency Check:** Verifies pipx is installed, installing it via Homebrew if absent.
- **Tool Installation:** Installs each tool using the specified method (Homebrew, pipx, or Git cloning).
- **Status Tracking:** Logs installation success or failure to a text file.
- **Report Generation:** Creates an HTML report with tool details, example commands, sources, and installation status.

### Output

Upon completion, the script outputs:

- A status log (`~/Desktop/rick_status.txt`) detailing the installation process.
- An HTML report (`~/Desktop/bluetooth_pentest_report.html`) opened in your default browser, summarizing tool installation results.

### Credits

- **Daniel Gillaspy:** Lead developer.
- **AI Assistance:** Supporting development and optimization.
- **Development Date:** March 20, 2025, with a nod to the chaotic genius of Rick Sanchez.

### License

This project is not licensed and offers no warranty.
```

This updated version includes better sectioning, a table for tool details, and clearer instructions for installation and usage.
