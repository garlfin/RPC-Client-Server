from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
from res.database.res.json import JSONReaderWriter
from res.rpc_enum import ErrorKeyType


class SimpleThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC',)


class RpcServer:
    response = "Hello"

    def __init__(self, databasepath):
        self.server = None
        self.identity = threading.get_ident()
        self.jsonRead = JSONReaderWriter(databasepath)
        self.jsonRead.readFile()
        self.statsFetched = None

    def printInfo(self, message, sender=None):
        if sender:
            print("[{0}-{1}] {2}".format(str(self.server.server_address), sender, message))
        else:
            print("[{0}] {1}".format(str(self.server.server_address), message))

    def close(self, reason=None):
        if reason:
            self.server.server_close()
        else:
            self.server.server_close()

    def initialize(self, address):
        self.server = SimpleThreadedXMLRPCServer(address, logRequests=False, requestHandler=RequestHandler)
        self.printInfo("Listening on port 8000")

    def retrieveStats(self, sender):
        self.statsFetched = self.jsonRead.retrieveFromJSON("Clients").get(sender)
        self.printInfo("Retrieved stats for {0}".format(sender), sender)
        if self.statsFetched:
            return [0, sender, str(self.statsFetched)]
        else:
            return [1, ErrorKeyType.notFound.value]

    def registerFunc(self, function_to_register):
        self.server.register_function(function_to_register)
        self.printInfo("Registered '" + function_to_register.__name__ + "' on server.")

    def register(self, functions):
        for x in functions:
            self.registerFunc(x)
        self.server.serve_forever()
