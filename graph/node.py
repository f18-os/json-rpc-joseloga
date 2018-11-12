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
            
    def convertToJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
              sort_keys=True)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

