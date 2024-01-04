import webview


def load_file_as_str(path: str) -> str:
    with open(path, "r") as f:
        content = f.read()
    return content


def load_css(w: webview.Window):  # close enough type checking
    w.load_css(load_file_as_str("web/css/output.css"))


if __name__ == "__main__":
    window = webview.create_window(title="", html=load_file_as_str("web/index.html"), width=300, height=400,
                                   resizable=False, text_select=True)
    webview.start(load_css, window)
