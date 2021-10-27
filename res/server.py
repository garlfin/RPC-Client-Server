from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
from res.database.res.json import jsonReaderWriter
from res.rpc_enum import errorKeyType

class SimpleThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class requestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC',)

class rpcServer:
    response = "Hello"

    def __init__(self, databasePath):
        self.server = None
        self.identity = threading.get_ident()
        self.jsonRead = jsonReaderWriter(databasePath)
        self.jsonRead.readFile()
        self.statsFetched = None

    def printInfo(self, message):
        print("[{0}] {1}".format(str(self.server.server_address), message))

    def close(self, reason = "Not specified"):
        self.server.server_close()

    def initialize(self, address):
        self.server = SimpleThreadedXMLRPCServer(address, logRequests=False,requestHandler=requestHandler)
        self.printInfo("Listening on port 8000")

    def retrieveStats(self, sender):
        self.statsFetched = self.jsonRead.retrieveFromJSON("Clients").get(sender)
        self.printInfo("Retrieved stats for {0}".format(sender))
        if self.statsFetched:
            return [0, sender, str(self.statsFetched)]
        else:
            return [1, errorKeyType.notFound.value]
    def registerFunc(self, function_to_register):
        self.server.register_function(function_to_register)
        self.printInfo("Registered '" + function_to_register.__name__ + "' on server.")

    def register(self, functions):
        for x in functions:
            self.registerFunc(x)
        self.server.serve_forever()
