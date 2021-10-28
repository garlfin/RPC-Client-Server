from enum import Enum


class KeyboardListener:
    """Its always listening 😈"""
    keyboardListenerDict = {
        "keyword_quit": "quit",
        "keyword_sendMessage": "sendMessage"
    }

    class DoIListen(Enum):
        listen = 0
        do_not_listen = 1

    def __init__(self, server_instance):
        self.Server = server_instance
        self.doIListen = False

    def status(self, do_or_do_not=None):
        """Turns the listening on or off, or does it? 😈 Also tells you if its listening or not."""
        if do_or_do_not:
            if do_or_do_not == self.DoIListen.listen:
                self.doIListen = True
                self.startListening()
            elif do_or_do_not == self.DoIListen.do_not_listen:
                self.doIListen = False
        else:
            return self.doIListen

    def startListening(self):
        self.Server.printInfo("I am always listening 😈 ")
        while self.doIListen:
            input_data = input()
            input_data_upper = input_data.upper()
            if input_data_upper == self.keyboardListenerDict.get("keyword_quit") .upper():
                self.Server.printInfo("Quitting")
                try:
                    self.Server.close()
                except OSError as err:
                    print(err)
