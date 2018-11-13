import json
class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

# here we convert the object in to a json format 
    def convertToJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
              sort_keys=True)

# this functions updates each node with their corresponding value 
# getting the value from the json graph(dictionary) modify by the server
def updateGraph(graph, jsonGraph):
    graph.val = jsonGraph['val'];
    for c in graph.children:
#        print(c.name, '---------- obj')
        for j in jsonGraph['children']:
            if c.name == j['name']:
#                print(j['name'], '====== json')
                updateGraph(c,j)

