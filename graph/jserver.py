# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket, json
from collections import namedtuple
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def swapper(self, txt):
    return ''.join(reversed(list(txt)))
  
  @request
  def increment(self,graph):
    graphs = json.loads(graph)
    print("incrementing graph...")
    items=graphs['children'] 
    graphs['val']+=1
    for item in items:
        print (item['name'])
        item['val']+=1
    return graphs    
    
    
#    return (x.children[0)
    
  @request
  def nop(self, txt):
    print(txt)
    return txt


# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
