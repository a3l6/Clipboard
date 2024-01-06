import gui
import ttkbootstrap as ttk
import threading
from clipboard import Clipboard
import pyautogui
import keyboard


def main():
    clipboard: Clipboard = Clipboard()

    mouse_pos = pyautogui.position()
    window = ttk.Window(
        title="",
        themename="darkly",
        size=(250, 350),
        resizable=(False, False),
        position=mouse_pos,
    )

    app = gui.Select_Menu(window, clipboard, hide)  # passing by reference?
    keyboard.add_hotkey("alt+c", show, args=(window,))
    clipboard_listener = threading.Thread(target=clipboard.listen, args=(app.update_clipboard,))
    clipboard_listener.start()
    app.mainloop()
    clipboard_listener.join()


def hide(window: ttk.Window):
    window.withdraw()


def show(window: ttk.Window):
    x, y = pyautogui.position()
    window.geometry(f"+{x - window.winfo_width()}+{y}")
    window.deiconify()


if __name__ == "__main__":
    main()