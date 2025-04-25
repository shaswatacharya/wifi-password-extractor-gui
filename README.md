<h1 align="center">Wi-Fi Password Extractor GUI - CYBER Mode 🚀</h1>

<table>
  <tr>
    <td>
      <p>
        Welcome to the <strong>Wi-Fi Password Extractor</strong> – the ultimate tool for extracting and managing saved Wi-Fi passwords on your Windows system.<br>
        With a sleek GUI and simple workflow, this tool is designed to make extracting, saving, and copying your Wi-Fi passwords a breeze.
      </p>
    </td>
    <td align="right">
      <img src="assets/images/app-icon.ico" width="120">
    </td>
  </tr>
</table>

---


## 📦 Features

- **Extract Saved Wi-Fi Passwords**: Easily retrieve the passwords for any Wi-Fi networks saved on your Windows system.
- **Save Passwords to File**: Securely store the passwords in a text file with timestamps.
- **Copy to Clipboard**: Instantly copy Wi-Fi passwords to your clipboard with a single click.
- **Speedtest**: Check your internet speed with a quick click to a speed test website.
- **Sleek & User-Friendly GUI**: Clean, modern design with smooth interactions for an optimal experience.

---

## 🛠️ Requirements

Before running the tool, make sure you have **Python 3.x** installed on your system. You will also need to install the necessary dependencies.

### Dependencies

- **Pillow**: For image handling (required to load icons and images).
- **tkinter**: For building the GUI (usually comes pre-installed with Python).

To install the required dependencies, run:

```bash
pip install Pillow
```

`tkinter` comes bundled with most Python installations, but if you encounter any issues, refer to the official tkinter documentation.

---

## 🚀 Installation

### 1. **Clone or Download**:
You have two options to get started:

- **Option 1**: Clone or download this repository to your local machine.

```bash
git clone https://github.com/shaswatacharya/wifi-password-extractor-gui.git
```

- **Option 2**: If you want to directly download the executable, **[click here to download wifi-pass-extract.exe](https://github.com/shaswatacharya/wifi-password-extractor-gui/wifi-pass-extract.exe)**.

### 2. **Navigate to Project Folder** (if cloning):
If you’ve cloned the repository, navigate to the project folder in your terminal or command prompt.

```bash
cd wifi-password-extractor-gui
```

### 3. **Install Dependencies** (for Python version only):
If you’re running the Python version of the application, install the required dependencies using pip.

```bash
pip install Pillow
```

`tkinter` should already be installed with Python, but if not, follow the installation instructions in the official tkinter documentation.

### 4. **Run the Application**:

#### **Option 1**: For Python version (requires Python and dependencies):
You can run the application by opening the `start.bat` file or directly executing the Python script:

```bash
python main.py
```
---

> ⚠️ **IMPORTANT:** This app does **NOT** run on its own by double-clicking `main.py`!  
> To launch the GUI, you must either:  
> 🔹 **Run** the `start.bat` file (recommended), **OR**  
> 🔹 Open terminal and run: `python main.py`


#### **Option 2**: For Executable version (no Python required):
If you’re using the precompiled `.exe` file, simply double-click the `wifi-pass-extract.exe` file to run the application. No need to install Python or any dependencies!

---

## 🎮 How to Use

1. **Run the Application**: Double-click the `start.bat` file, which will launch the GUI. If you're running it via Python, execute `python main.py`.
   
2. **Extract Wi-Fi Passwords**: Click the **"🔍 Extract Passwords"** button to fetch all the saved Wi-Fi credentials from your system.
   
3. **Copy Password**: For each Wi-Fi network, click the **"📋 Copy"** button next to it to copy the password to your clipboard.

4. **Save Passwords**: After extracting passwords, click **"💾 Save Passwords"** to save them into a text file named `wifi_passwords.txt`. This file will be stored in the project directory.

5. **Speedtest**: Check your internet speed by clicking the **"⚡ Speedtest"** button. This will open a speed test website in your browser for real-time results.

---

## 💡 Customization

The app is modular, clean, and easy to customize. Here are a few ways you can modify the tool:

- **UI Changes**: You can easily modify the look and feel by editing the `main.py` file. Change the fonts, colors, and layout to match your preferences.
- **Add More Features**: Want to add a new feature? Modify or extend the existing functions like `get_wifi_names()` or `get_wifi_password()` to add more capabilities (e.g., network scanning, automated login, etc.).
- **Personalized Icon**: Replace the app icon by placing a new `.ico` file in the `assets/images/` folder.

The code is easy to follow and well-structured, so feel free to modify it and make it your own!

---

## 🤝 Contributing

Wanna level up this project together? Contributions are more than welcome! 🚀

- Fork the repo 🍴  
- Create a new branch 💡  
- Make your magic happen 🔧  
- Open a pull request 🛠️  

Let's collab and make this even more awesome for devs around the world 🌐💻💙


---

## 📝 License

This project is licensed under the **MIT License**. You can freely modify, distribute, and use it for both personal and commercial purposes. For more details, refer to the [LICENSE](LICENSE) file.

---

## 📞 Contact

Have questions or need support? Feel free to reach out!

- **GitHub Issues**: [Report an Issue](https://github.com/shaswatacharya/wifi-password-extractor-gui/issues)
- **GitHub**: [github.com/shaswatacharya](https://github.com/shaswatacharya)

---
