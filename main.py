import subprocess
import re
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os
from PIL import Image, ImageTk  # Image handling
import webbrowser

wifi_entries = []  # List to store Wi-Fi entries and buttons
photo_images = {}  # Store images to prevent GC issues

def get_wifi_names():
    try:
        profiles_data = subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL).decode(errors="ignore")
        profiles = re.findall(r"All User Profile\s*: (.*)", profiles_data)
        return [p.strip() for p in profiles]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch Wi-Fi names.\n{e}")
        return []

def get_wifi_password(ssid):
    try:
        detail = subprocess.check_output(f'netsh wlan show profile name="{ssid}" key=clear', shell=True, stderr=subprocess.DEVNULL).decode(errors="ignore")
        password_match = re.search(r"Key Content\s*: (.*)", detail)
        return password_match.group(1) if password_match else "None"
    except subprocess.CalledProcessError:
        return "Access Denied"

def show_passwords():
    for ssid, label, copy_btn in wifi_entries:
        password = get_wifi_password(ssid)
        label.config(text=f"{ssid} → {password}")
        copy_btn.config(command=lambda pwd=password: copy_single(pwd))
        copy_btn.pack(side=tk.RIGHT)  # Show copy button now

def copy_single(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    messagebox.showinfo("Copied", f"Password Copied:\n{text}")

def save_passwords():
    if not wifi_entries:
        messagebox.showerror("Error", "No Wi-Fi data to save.")
        return

    if all(label.cget("text").endswith("→ 🔒") for ssid, label, _ in wifi_entries):
        messagebox.showwarning("Warning", "Please extract Wi-Fi passwords before saving.")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wifi_passwords.txt")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"\n=== Saved on {now} ===\n")
        for ssid, label, _ in wifi_entries:
            password = label.cget("text").split("→")[-1].strip()
            file.write(f"{ssid} → {password}\n")

    messagebox.showinfo("Saved", f"Passwords saved to:\n{file_path}")

def open_instructions():
    os.startfile("https://github.com/yourusername/yourproject")

#Little Shortcut :) K code herira

def speedtest():
    webbrowser.open("https://fast.com")  # Speedtest link

# GUI Setup
root = tk.Tk()
root.title("Wi-Fi Password Extractor - CYBER Mode 🚀")
root.geometry("700x540")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Load Wi-Fi icon
wifi_icon = ImageTk.PhotoImage(Image.open(os.path.join("assets", "images", "wifi-icon.png")).resize((20, 20)))
photo_images['wifi'] = wifi_icon

root.iconbitmap(os.path.join("assets", "images", "app-icon.ico"))

# Fonts and Styles
title_font = ("Segoe UI", 18, "bold")
body_font = ("Arial", 13)
button_font = ("Segoe UI", 12, "bold")

tk.Label(root, text="📡 Wi-Fi Password Extractor", font=title_font, bg="#f0f0f0").pack(pady=10)

password_frame = tk.Frame(root, bg="#f0f0f0")
password_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Create Wi-Fi entries (SSIDs)
wifi_entries.clear()
for ssid in get_wifi_names():
    entry_frame = tk.Frame(password_frame, bg="#f0f0f0")
    entry_frame.pack(pady=5, fill=tk.X, padx=20)

    wifi_icon_label = tk.Label(entry_frame, image=wifi_icon, bg="#f0f0f0")
    wifi_icon_label.pack(side=tk.LEFT, padx=5)

    label = tk.Label(entry_frame, text=f"{ssid} → 🔒", font=body_font, anchor="w", bg="#f0f0f0")
    label.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    copy_btn = ttk.Button(entry_frame, text="📋 Copy", width=10)
    wifi_entries.append((ssid, label, copy_btn))

# Button Style (Rounded, Custom Padding)
style = ttk.Style()
style.configure("Rounded.TButton", font=button_font, padding=10, relief="flat")
style.map("Rounded.TButton",
          relief=[('pressed', 'sunken'), ('active', 'groove')],
          background=[('!disabled', '#0078D7')],
          foreground=[('pressed', 'white'), ('active', 'black')])

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# Align Buttons in Grid
extract_btn = ttk.Button(button_frame, text="🔍 Extract Passwords", command=show_passwords, width=20, style="Rounded.TButton")
extract_btn.grid(row=0, column=0, padx=15, pady=10)

save_btn = ttk.Button(button_frame, text="💾 Save Passwords", command=save_passwords, width=20, style="Rounded.TButton")
save_btn.grid(row=0, column=1, padx=15, pady=10)

# Footer Label
footer_label = tk.Label(root, text="🌀 Made by Shaswat", font=("Segoe UI", 10), bg="#f0f0f0")
footer_label.pack(pady=10)

# Instructions Button
instructions_btn = ttk.Button(root, text="📘 Read Instructions", command=open_instructions, width=18)
instructions_btn.pack(side=tk.BOTTOM, anchor="se", padx=15, pady=5)

# Speedtest Button
speedtest_btn = ttk.Button(root, text="⚡ Speedtest", command=speedtest, width=18)
speedtest_btn.pack(side=tk.BOTTOM, anchor="se", padx=15, pady=0)

root.mainloop()
