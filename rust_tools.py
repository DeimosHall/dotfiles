#!/bin/python3
import os

os_type = os.popen("uname -a").read()
user_name = os.popen("whoami").read().splitlines()[0]

if "Ubuntu" in os_type or "Debian" in os_type:
    print("Debian/Ubuntu based")
    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")
    os.system("sudo apt install build-essential -y")
    os.system("sudo apt install cmake -y")
    os.system("sudo apt install curl -y")
    os.system("sudo apt-get install libfontconfig libfontconfig1-dev -y")

if "fedora" in os_type:
    print("Fedora")
    os.system("sudo dnf update -y")
    os.system("sudo dnf install cmake -y")

# Check if Rust is installed
if os.path.exists(f"/home/{user_name}/.cargo/bin/rustc"):
    print("[*] Rust is already installed")
else:
    print("[*] Installing Rust")
    os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")
    os.system("Reboot your system and run this script again")
    exit()

# Check if every tool is installed
print(f"/home/{user_name}/.cargo/bin/bottom")
if os.path.exists(f"/home/{user_name}/.cargo/bin/btm"):
    print("[*] bottom is already installed")
else:
    print("[*] Installing bottom")
    os.system("cargo install bottom")

if os.path.exists(f"/home/{user_name}/.cargo/bin/starship"):
    print("[*] starship is already installed")
else:
    print("[*] Installing starship")
    os.system("cargo install starship --locked")
    os.system("echo 'eval \"$(starship init bash)\"' >> ~/.bashrc")

if os.path.exists(f"/home/{user_name}/.cargo/bin/bat"):
    print("[*] bat is already installed")
else:
    print("[*] Installing bat")
    os.system("cargo install bat --locked")
    os.system("echo \"alias cat='bat'\" >> ~/.bashrc")

if os.path.exists(f"/home/{user_name}/.cargo/bin/exa"):
    print("[*] exa is already installed")
else:
    print("[*] Installing exa")
    os.system("cargo install exa")
    os.system("echo \"alias ls='exa'\" >> ~/.bashrc")

print("Installation completed | Reboot your system to apply changes")