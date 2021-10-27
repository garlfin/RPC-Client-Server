import res.server as server
import res.client as client
import threading
import os

address = ("localhost", 8000)
dataPath = os.getcwd()+"/res/database/clients/db.json"


def startServer():
    Server = server.rpcServer(dataPath)
    Server.initialize(address)
    Server.register([Server.respond, Server.retrieveStats])


def StartClient(client_name):
    identity = threading.current_thread().ident
    try:
        Client = client.rpc_client(client_name)
        Client.listen(client.getDomainFromAddress(address))
        Client.sendMessage()
    except ConnectionRefusedError:
        print("[" + str(client_name) + "] Machine refused connection.")


currentWorkingThreads = [threading.Thread(target=startServer), threading.Thread(target=StartClient, args=["0442246"]),
                         threading.Thread(target=StartClient, args=["5561111"])]

for thread in currentWorkingThreads:
    thread.start()
for thread in currentWorkingThreads:
    thread.join()
