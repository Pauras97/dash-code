# // We want to implement an in-memory tree key value store for Doordash Restaurant Menus.
# // Definitions:

# // path is a / separate string describing the node. Example /Tres Potrillos/tacos/al_pastor
# // Values are all strings
# // API spec:
# // get(path): String -> returns the value of the node at the given path
# // create(path, value) -> creates a new node and sets it to the given value. 
#Should error out if the node already exists or if the node’s parent does not exist. 
#That is /Sweetgreen/naan_roll cannot be created if /Sweetgreen has not already been created
# // delete(path) -> deletes a node, but ONLY if it has no children

class Trie(object):
    def __init__(self, name):
        self.map = defaultdict(Trie)
        self.name = name
        self.value = -1

class MenuPath:
    def __init__(self):
        self.root = Trie("")
    
    def get(self, path):
        cur = self.root
        paths = path.split("/")
        
        for i in range(1, len(paths)):
            name = paths[i]
            
            if name not in cur.map:
                return -1
            cur = cur.map[name]
        return cur.value
    
    def create(self, path, value):
        cur = self.root
        paths = path.split("/")
        
        for i in range(1, len(paths)):
            name = paths[i]
            
            if name not in cur.map:
                if i == len(paths)-1:
                    cur.map[name] = Trie(name)
                else:
                    return False
            cur = cur.map[name]
        
        if cur.value != -1:
            return False
        cur.value = value
        
        return True
    
    def delete(self, path):
        cur = self.root
        paths = path.split("/")
        delete = False
        
        for i in range(1, len(paths)):
            name = paths[i]
            
            if i == len(paths)-1:
                if not bool(cur.map[name].map):
                    delete = True
            
            cur = cur.map[name]
        
        if delete:
            del self.root.map[paths[1]]
        
        for key in self.root.map:
            print(self.root.map[key].name)

menu = MenuPath()
print(menu.create("/Tres Potrillos", 2))
print(menu.create("/Tres Potrillos/tacos", 3))
print(menu.create("/Tres Potrillos/tacos/al_pastor", 4))
print(menu.create("/leet/code",2))
print(menu.create("/leet",1))
print(menu.get("/Tres Potrillos/tacos/al_pastor"))
print(menu.get("/leet/code"))
print(menu.delete("/Tres Potrillos"))
print(menu.delete("/leet"))


                