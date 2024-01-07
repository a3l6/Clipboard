import ttkbootstrap as ttk
from typing import Callable
import threading
from clipboard import Clipboard


class Controller:       # This will control all threads to shut them off
    def __init__(self):
        self._on = True
        self.visible = False
        self.window: ttk.Window | None = None
        self.hide_func: Callable | None = None
        self._threads: list[threading.Thread] = []
        self.clipboard: Clipboard | None = None

    def status(self) -> bool:
        return self._on

    def set_window(self, window: ttk.Window):
        self.window = window

    def set_clipboard(self, clipboard: Clipboard):
        self.clipboard = clipboard

    def set_hide_func(self, func: Callable):
        self.hide_func = func

    def hide(self, x, y, Button, pressed):
        if not self._on: raise SystemExit
        if self.window.focus_get() is None: self.hide_func(self.window)

    def register_thread(self, thread: threading.Thread):
        self._threads.append(thread)

    def shutdown(self):
        self._on = False
        self.window.destroy()
        self.clipboard.running = False
        for thread in self._threads:
            thread.join()
        quit()
