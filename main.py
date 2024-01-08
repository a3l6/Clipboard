import gui
import ttkbootstrap as ttk
import threading
from clipboard import Clipboard
from controller import Controller
import pynput.mouse as pynput


def main():
    # Initialize everything
    clipboard: Clipboard = Clipboard(controller)
    controller.set_clipboard(clipboard)

    mouse_pos = mouse.position
    window = ttk.Window(
        title="",
        themename="darkly",
        size=(250, 350),
        resizable=(False, False),
        position=mouse_pos,
    )
    controller.set_window(window)

    app = gui.Select_Menu(window, clipboard, controller.hide)  # passing by reference?

    hotkey = threading.Thread(target=controller.hotkey_listener)
    hotkey.start()
    controller.register_thread(hotkey)

    clipboard_listener = threading.Thread(target=clipboard.listen, args=(app.update_clipboard,))
    clipboard_listener.start()
    controller.register_thread(clipboard_listener)

    window.protocol("WM_DELETE_WINDOW", controller.shutdown)

    app.mainloop()


if __name__ == "__main__":
    controller = Controller()
    mouse = pynput.Controller()

    click_listener = pynput.Listener(on_click=controller.hide)
    click_listener.start()
    controller.register_thread(click_listener)

    main()
