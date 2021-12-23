import requests
from skpy import SkypeEventLoop, SkypeNewMessageEvent, Skype
import os
from dotenv import load_dotenv

load_dotenv()


class SkypeListener(SkypeEventLoop):
    def __init__(self):
        username = os.getenv('email')
        password = os.getenv('password')
        self.sk = Skype(os.getenv('email'), os.getenv('password'))
        super(SkypeListener, self).__init__(username, password)

    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent):
            default = "Skype listener: Investigate if you see this."
            if not event.msg.userId == self.userId:
                message = {
                    "user_id": event.msg.userId,
                    "chat_id": event.msg.chatId,
                    "msg": event.msg.content
                }
                print(message)
                if message['msg'] == '<ss type="hi">(hi)</ss>' or message['msg'] == '<ss type="1f44b_wavinghand">(wavinghand)</ss>':
                    response = requests.post('http://td-report.loc/api/attendance/update', data=message)
                    if response.status_code == 200:
                        data = response.json()
                        if data['status'] == 'success':
                            try:
                                ch = self.sk.contacts[event.msg.userId].chat
                                ch.sendMsg(data['message'])
                            except:
                                return 0
