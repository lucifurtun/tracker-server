# Connected to websocket.connect
from channels import Group


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("tracking").add(message.reply_channel)


def ws_message(message):
    print(message.content)
    Group("tracking").send({
        "text": "[user] %s" % message.content['text'],
    })


def ws_disconnect(message):
    Group("tracking").discard(message.reply_channel)
