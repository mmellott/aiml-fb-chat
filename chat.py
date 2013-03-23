#!/usr/bin/python
import sleekxmpp
import aiml
import bot
#import logging
#logging.basicConfig(level=logging.DEBUG)

pass = raw_input("password: ")

jid = 'alice.mellott.1@chat.facebook.com'
password = pass 
server = ('chat.facebook.com', 5222)

chatbot = bot.AliceBot(jid,password)
#chatbot.add_event_handler('session_start', session_start)
#chatbot.add_event_handler('message', message)
chatbot.auto_reconnect = True
chatbot.connect(server)
chatbot.process(block=True)
