import os
import subprocess
import keyboard
import pystray
from PIL import Image
import threading

class WezTermTray:
    def __init__(self, icon_path):
        self.icon = pystray.Icon("wezterm_tray", Image.open(icon_path), "WezTerm Tray", menu=self.create_menu())
        threading.Thread(target=self.run_tray, daemon=True).start()
        self.setup_hotkeys()

    def create_menu(self):
        menu = pystray.Menu(
            pystray.MenuItem("Exit", self.exit_action)
        )
        return menu

    def exit_action(self, icon, item):
        icon.stop()
        os._exit(0)

    def setup_hotkeys(self):
        keyboard.add_hotkey('alt+f1', self.open_wezterm)
        keyboard.wait('esc')

    def open_wezterm(self):
        subprocess.Popen(
            ['C:\\Program Files\\WezTerm\\wezterm.exe', 'start', '-e', 'ollama', 'run', 'llama3.2'],
            creationflags=subprocess.CREATE_NO_WINDOW
        )

    def run_tray(self):
        self.icon.run()

if __name__ == "__main__":
    icon_path = "E:\\Developer\\Program\\Python\\run_ollama\\20230315_144251.ico"
    WezTermTray(icon_path)

