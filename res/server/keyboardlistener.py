class KeyboardListener:
    """Its always listening >:)))))))"""
    keyboardListenerDict = {
        "keyword_quit": "quit",
        "keyword_sendMessage": "sendMessage"
    }

    def __init__(self, server_instance):
        self.Server = server_instance
        self.DoIListen = False

    def enable(self):
        self.DoIListen = True
        self.startListening()

    def disable(self):
        self.DoIListen = False

    def startListening(self):
        self.Server.printInfo("I am listening >:)")
        while self.DoIListen:
            input_data = input()
            input_data_upper = input_data.upper()
            if input_data_upper == self.keyboardListenerDict.get("keyword_quit") .upper():
                self.Server.printInfo("Quitting")
                try:
                    self.Server.close()
                except OSError as err:
                    print(err)
