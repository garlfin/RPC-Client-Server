import xmlrpc.client

def getDomainFromAddress(address):
    return "http://" + address[0] + ":" + str(address[1]) + "/"

class rpc_client: 
    def __init__(self, name):
        self.name = name
        self.proxy = None
        self.returnedStats = None
    def printInfo(self, message):
        print("[{0}] {1}".format(self.name, message))
    def errorHandler(self, err):
        self.printInfo("A fault occurred")
        self.printInfo("Fault code: %d" % err.faultCode)
        self.printInfo("Fault string: %s" % err.faultString)
    def listen(self, domain):
        self.printInfo("Using domain " + domain)
        try:
            self.proxy = xmlrpc.client.ServerProxy(domain)
        except xmlrpc.client.Fault as err:
            self.errorHandler(err)
    def whatsMyName(self):
        self.printInfo("My name is " + self.name + ".") 
    def sendMessage(self):
        self.printInfo("Sent " + self.name + " on port 8000")
        #self.printInfo(self.proxy.respond(self.name))
        self.returnedStats = self.proxy.retrieveStats(str(self.name))
        if self.returnedStats[0] == 0:
            self.printInfo("[{0}: ".format(self.returnedStats[1]) + self.returnedStats[2]+"]")
        else:
            if self.returnedStats[0] == 1:
                self.printInfo("[ERROR] Stats not found!")
