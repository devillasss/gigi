<div align="center">

# 🖱️ GIGI

A lightweight Python utility that prevents screen timeout by simulating mouse movement.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

---

## 🚀 Quick Start

1. Install dependencies:
   ```bash
   pip install pyautogui
   ```

2. Run the script:
   ```bash
   python3 gigi.py
   ```

## ⚙️ Configuration

### Command Line Options

| Flag | Description | Default |
|------|-------------|---------|
| `-d, --duration` | Movement duration (seconds) | 15 |
| `-p, --pause` | Pause between moves (seconds) | 10 |
| `-s, --start-y` | Starting Y position | 20 |
| `--dry-run` | Preview settings only | - |

### Examples

# Run with custom duration
python3 gigi.py -d 10

# Run with custom pause
python3 gigi.py -p 5

# Preview settings
python3 gigi.py --dry-run

## ⌨️ Keyboard Shortcuts Setup

### Ubuntu/Debian

1. **Create Application Launcher**
   ```bash
   # Create a new .desktop file
   nano ~/.local/share/applications/gigi.desktop
   ```

   Add the following content:
   ```ini
   [Desktop Entry]
   Name=GIGI Mouse Mover
   Comment=Prevent screen timeout
   Exec=python3 /full/path/to/gigi.py
   Type=Application
   Terminal=true
   Categories=Utility;
   ```

2. **Setup Start Shortcut**
   - Open Settings → Keyboard
   - Navigate to "Keyboard Shortcuts" → "Custom Shortcuts"
   - Click "+" to add new shortcut
   - Name: `Start GIGI`
   - Command: `python3 /full/path/to/gigi.py`
   - Click "Set Shortcut" and press `Ctrl + Alt + G`

3. **Setup Stop Shortcut**
   - Click "+" to add another shortcut
   - Name: `Stop GIGI`
   - Command: `/full/path/to/kill_gigi.sh`
   - Click "Set Shortcut" and press `Ctrl + Alt + K`

### Default Shortcuts
| Action | Shortcut |
|--------|----------|
| Start GIGI | `Ctrl + Alt + G` |
| Stop GIGI | `Ctrl + Alt + K` |
| Terminal Stop | `Ctrl + C` |

> **Note**: Replace `/full/path/to/` with your actual script path

## 🛑 Stopping Methods

1. **Keyboard Shortcut**: Press `Ctrl + Alt + K`
2. **Terminal**: Press `Ctrl + C`
3. **Kill Script**: Run `pkill -f "/full/path/to/gigi.py"`

## 💡 How It Works

The script moves your mouse cursor in a pattern:
- Start at top-left
- Move to middle-left
- Pause
- Repeat cycle

Default timings:
- Movement: 15 seconds
- Pause: 10 seconds

---

<div align="center">
Made with ❤️ for those long meetings
</div>
