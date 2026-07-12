import webview
from datetime import datetime

class Api:
    def get_time(self):
        now = datetime.now()

        return {
            "time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%A, %d %B %Y")
        }

api = Api()

window = webview.create_window(
    "Clock",
    "index.html",
    js_api=api,
    width=450,
    height=250,
    resizable=False
)

webview.start()
