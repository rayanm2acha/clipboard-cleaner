#!/usr/bin/env python3
"""
Clipboard Cleaner
-----------------
A tiny cross-platform utility to wipe your clipboard content.
"""

import subprocess
import platform
import sys

def clear_clipboard():
    system = platform.system()

    try:
        if system == "Darwin":
            subprocess.run("pbcopy < /dev/null", shell=True, check=True)
        elif system == "Linux":
            subprocess.run("xclip -selection clipboard < /dev/null", shell=True, check=True)
        elif system == "Windows":
            subprocess.run("echo off | clip", shell=True, check=True)
        else:
            print(f"Unsupported OS: {system}")
            return False
        return True
    except Exception as e:
        print(f"Error clearing clipboard: {e}")
        return False


if __name__ == "__main__":
    success = clear_clipboard()
    if success:
        print("✅ Clipboard cleared.")
        sys.exit(0)
    else:
        print("❌ Failed to clear clipboard.")
        sys.exit(1)