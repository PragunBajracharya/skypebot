from threading import Thread

from bot import app
from bot.SkypeListener import SkypeListener


def runSkypeListener():
    sl = SkypeListener()
    sl.loop()


if __name__ == '__main__':
    Thread(target=runSkypeListener).start()
    app.run(debug=True, use_reloader=False)
