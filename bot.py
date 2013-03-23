from sleekxmpp import ClientXMPP
import aiml
from random import randrange
import time

class AliceBot(ClientXMPP):

    # the one and only ctor
    def __init__(self, jid, password, name):
        # init xmpp stuff
        ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

        # init alice stuff
        self._k = aiml.Kernel()
        self._k.learn("std-startup.xml")
        self._k.respond("load aiml b")
        self._k.setBotPredicate("name",name)

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
            resp = self._k.respond(msg['body'], msg['from'])

            # try to not look like a bot?
            time.sleep(randrange(0,3))

            # reply
            msg.reply(resp).send()

