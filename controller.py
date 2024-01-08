import ttkbootstrap as ttk
import threading
from clipboard import Clipboard
import pynput.mouse as pynput
from pynput import keyboard


class Controller:       # This will control all threads to shut them off
    def __init__(self):
        self._on = True
        self.visible = False
        self.window: ttk.Window | None = None
        self._threads: list[threading.Thread] = []
        self.clipboard: Clipboard | None = None

    def status(self) -> bool:
        return self._on

    def set_window(self, window: ttk.Window):
        self.window = window

    def set_clipboard(self, clipboard: Clipboard):
        self.clipboard = clipboard

    def hide(self, x=None, y=None, Button=None, pressed=None, force=False):
        print(f"{self._on=}")
        if not self._on: raise SystemExit
        if self.window.focus_get() is None and not force:
            print("hiding")
            self.visible = False
            self.window.withdraw()
        elif force:
            self.visible = False
            self.window.withdraw()

    def show(self):
        if not self._on: raise SystemExit
        self.visible = True
        mouse = pynput.Controller()
        x, y = mouse.position
        self.window.geometry(f"+{x - self.window.winfo_width()}+{y}")
        self.window.deiconify()

    def register_thread(self, thread: threading.Thread):
        self._threads.append(thread)

    def shutdown(self):
        self._on = False
        self.window.destroy()
        self.clipboard.running = False
        for thread in self._threads:
            thread.join()
        quit()

    def hotkey_listener(self):
        with keyboard.GlobalHotKeys({'<cmd_l>+v': self.show}) as h:
            h.join()
