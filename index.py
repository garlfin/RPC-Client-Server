import res.server.server as server
import res.client as client
import threading
import os
import res.server.keyboardlistener

address = ("localhost", 8000)
dataPath = os.getcwd()+"/res/database/clients/db.json"


def startServer():
    Server = server.RpcServer(dataPath)
    Server.initialize(address)
    KeyboardListener = res.server.keyboardlistener.KeyboardListener(Server)
    threading.Thread(target=KeyboardListener.enable).start()
    Server.register([Server.retrieveStats, Server.close])


def StartClient(client_name):
    try:
        client_thread = client.RPCClient(client_name)
        client_thread.listen(client.getDomainFromAddress(address)+"RPC")
        client_thread.receiveStats()
    except ConnectionRefusedError:
        print("[" + str(client_name) + "] Machine refused connection.")


currentWorkingThreads = [threading.Thread(target=startServer), threading.Thread(target=StartClient, args=["0442246"]),
                         threading.Thread(target=StartClient, args=["5561111"])]

for thread in currentWorkingThreads:
    thread.start()
for thread in currentWorkingThreads:
    thread.join()
