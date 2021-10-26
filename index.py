import res.server as server
import res.client as client
import threading

address = ("localhost", 8000)
dataPath = "c:/Users/0442246/OneDrive - Miami-Dade County Public Schools/Desktop/bbfl/rpc/py/res/database/res/testfile.json"

def startServer():
    Server = server.rpc_server(dataPath)
    Server.initialize(address)
    Server.register([Server.respond, Server.retrieveStats])

def StartClient(client_name):
    identity = threading.current_thread().ident
    try:
        Client = client.rpc_client(client_name)
        Client.listen(client.getDomainFromAddress(address))
        Client.sendMessage()
    except ConnectionRefusedError:
                print("["+str(client_name)+"] Machine refused connection.")

Threads = []
Threads.append(threading.Thread(target = startServer))
Threads.append(threading.Thread(target = StartClient, args = ["0442246"]))
Threads.append(threading.Thread(target = StartClient, args = ["galim"]))

for x in Threads:
    x.start()
for x in Threads:
    x.join()

