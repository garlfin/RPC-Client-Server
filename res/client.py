import xmlrpc.client
from res.rpc_enum import ErrorKeyType, errorSyn


def getDomainFromAddress(address, ssl=False):
    if ssl:
        return "https://" + address[0] + ":" + str(address[1]) + "/"
    else:
        return "http://" + address[0] + ":" + str(address[1]) + "/"


class RPCClient:
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

    # def close(self):
    #   self.proxy.close()

    def whatsMyName(self):
        self.printInfo("My name is %s." % self.name)

    def receiveStats(self):
        self.printInfo("Sent %s on port 8000" % self.name)
        self.returnedStats = self.proxy.retrieveStats(str(self.name))
        if self.returnedStats[0] == 0:
            self.printInfo("[{0}: ".format(self.returnedStats[1]) + self.returnedStats[2] + "]")
        else:
            if self.returnedStats[0] == 1:
                self.printInfo(errorSyn[ErrorKeyType(self.returnedStats[1])])
