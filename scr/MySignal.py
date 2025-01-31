from PySide6.QtCore import Signal, QObject
class SignalBridge(QObject):
    message_received = Signal(str)
class SignalSaveFriend(QObject):
    message_received = Signal(str,list)
getPrivateMessage = SignalBridge()
SaveMessageList = SignalSaveFriend()