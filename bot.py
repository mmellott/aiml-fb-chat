from sleekxmpp import ClientXMPP
import aiml
from random import randrange
import time

class AliceBot(ClientXMPP):

    # the one and only ctor
    def __init__(self, jid, password):
        # init xmpp stuff
        ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

        # init alice stuff
        self.__k = aiml.Kernel()
        self.__k.learn("std-startup.xml")
        self.__k.respond("load aiml b")

    # don't really understand what a session is
    def session_start(self, event):
        self.send_presence()
        print "session started"
        self.get_roster()


    # handle message with aiml response
    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):

            # get response
            # super easy sessions!
            resp = self.__k.respond(msg['body'], msg['from'])

            # try to not look like a bot?
            time.sleep(randrange(0,3))

            # reply
            msg.reply(resp).send()

