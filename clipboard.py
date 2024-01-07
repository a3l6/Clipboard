import pyperclip as pc
from typing import Callable


class Clipboard:
    def __init__(self, controller):
        self._ch: list[str] = []# ["123456789123456789123456789", "This", "Should", "Work", "Working test"]  # Cliboard history
        self.running = True
        self.controller = controller

    def __len__(self) -> int:
        return len(self._ch)

    def clipboard_history(self):
        return self._ch[::-1]

    def listen(self, callback: Callable):
        while self.controller.status():
            text: str = pc.waitForNewPaste()
            if text in self._ch: self._ch.remove(text)
            self._ch.append(text)
            callback()
        raise SystemExit
