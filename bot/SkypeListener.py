from skpy import SkypeEventLoop, SkypeNewMessageEvent
import os
from dotenv import load_dotenv

load_dotenv()


class SkypeListener(SkypeEventLoop):
    def __init__(self):
        username = os.getenv('email')
        password = os.getenv('password')
        super(SkypeListener, self).__init__(username, password)

    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent):
            default = "Skype listener: Investigate if you see this."
            if not event.msg.userId == self.userId:
                message = {"user_id": event.msg.userId,
                           "chat_id": event.msg.chatId,
                           "msg": event.msg.content}
                print(message)
