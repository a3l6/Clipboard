import webview


def load_html_as_str(path: str) -> str:
    with open(path, "r") as f:
        content = f.read()
    return content


webview.create_window(title="", html=load_html_as_str("web/index.html"), width=300, height=400, resizable=False)
webview.start()
