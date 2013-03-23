#!/usr/bin/python
import sleekxmpp
import aiml
import bot
import signal
import sys
#import logging
#logging.basicConfig(level=logging.DEBUG)

password = raw_input("password: ")
jid = 'alice.mellott.1@chat.facebook.com'
server = ('chat.facebook.com', 5222)

chatbot = bot.AliceBot(jid,password)
chatbot.auto_reconnect = True
chatbot.connect(server)
chatbot.process(block=False)

# exit with grace
def sigint_handler(signal, frame):
        print "exit time"

        global chatbot
        chatbot.disconnect(wait=True)        
        sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

while True:
    pass
