# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from node import *
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server =  rpc.get_peer_proxy()
# Execute in server:

#here we create the data structure a root with 3 childs
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()

#here we received the graph incremented from the server
jsonGraph=server.increment(root.convertToJSON())
print (jsonGraph)

#here we update the graph with the new info from the 
updateGraph(root,json.loads(jsonGraph))

print("graph after increment")
root.show()
rpc.close() # Closes the socket 's' also



