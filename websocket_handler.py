from PyQt5.QtCore import QObject, pyqtSignal, QUrl
from PyQt5.QtWebSockets import QWebSocket


class WebSocketHandler(QObject):
    messageReceived = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.websocket = QWebSocket(parent)
        self.websocket.textMessageReceived.connect(self.handleMessage)
        # Replace 'your_websocket_url' with your actual WebSocket server URL
        self.websocket.open(QUrl("ws://127.0.0.1:7890"))

    def handleMessage(self, message):
        self.messageReceived.emit(message)

    def SendMessage(self):
        self.websocket.sendTextMessage("Mute_alarms")
