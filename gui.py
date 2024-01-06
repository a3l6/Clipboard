import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip
from utils.limit_chars import limit_chars
from typing import Callable


class Clipboard_Content_Button(ttk.Button):
    def __init__(self, master, text, real_text, hide: Callable, window, *args, **kwargs):
        super().__init__(master, padding=8, command=self._copy_to_clipboard, text=text, *args, **kwargs)
        self.text = text
        self.real_text = real_text
        self.hide = hide
        self.window = window

    def _copy_to_clipboard(self):
        pyperclip.copy(self.real_text)
        self.hide(self.window)


class Select_Menu(ttk.Frame):
    def __init__(self, master, clipboard, hide: Callable):
        super().__init__(master, padding=10)
        self.master = master
        self.hide = hide

        self.pack(fill=BOTH, expand=YES)

        # create title
        self.title = ttk.Label(self, text="Clipboard++", font="TkFixedFont 12")
        self.title.configure(justify=CENTER)
        self.title.pack()

        self.clipboard = clipboard

        self.btns: list[Clipboard_Content_Button] = []
        # Create buttons
        if len(clipboard) == 0:  #26
             self.placeholder = ttk.Label(self, text="Nothing yet...", font="TkFixedFont 10", padding=10)
             self.placeholder.pack()
        else:
            for i in range(len(clipboard)):
                btn = Clipboard_Content_Button(self, text=limit_chars(clipboard.clipboard_history()[i], 26, True),
                                               bootstyle=SECONDARY, width=200, real_text=clipboard.clipboard_history()[i],
                                               hide=self.hide, window=self.master)
                btn.pack(pady=10)
                self.btns.append(btn)
        self.hide(window=master)

    def update_clipboard(self):
        for btn in self.btns:
            btn.pack_forget()
        for i in range(len(self.clipboard)):
            btn = Clipboard_Content_Button(self, text=limit_chars(self.clipboard.clipboard_history()[i], 26,
                                        True), real_text=self.clipboard.clipboard_history()[i],
                                                bootstyle=SECONDARY, width=200, hide=self.hide, window=self.master)
            btn.pack(pady=10)
            self.btns.append(btn)
        if len(self.btns) > 0: self.placeholder.pack_forget()
