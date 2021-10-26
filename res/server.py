import threading
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
from res.database.res.json import jsonReaderWriter

class SimpleThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class rpc_server:
    response = "Hello"
    def __init__(self, databasePath):
        self.server = None
        self.identity = threading.get_ident()
        self.jsonRead = jsonReaderWriter(databasePath)
        self.jsonRead.readFile()
        self.statsFetched = None
    def printInfo(self, message):
        print("[{0}] {1}".format(str(self.identity), message))
    def initialize(self, address):
        self.server = SimpleThreadedXMLRPCServer(address)
        self.printInfo("Listening on port 8000")
    def respond(self, sender):
        return self.response + " " + sender + "!"
    def retrieveStats(self, sender):
        self.statsFetched = self.jsonRead.retrieveFromJSON("Clients").get(sender)
        if self.statsFetched:
            return [0, sender, str(self.statsFetched)]
        else:
            return [1]
    def registerFunc(self, function_to_register):
        self.server.register_function(function_to_register)
        self.printInfo("Registered '" + function_to_register.__name__ +"' on server.")
    def register(self, functions):
        for x in functions:
            self.registerFunc(x)
        self.server.serve_forever()

       
    