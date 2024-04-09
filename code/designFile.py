# Round 1: Design File System (Trie solution)
# Implement an in-memory key-value store, for storing a value in a specific path.

# Definitions:

# Path is a "/" separated string (e.g. "/first/second")
# Value are all strings (e.g. "value")
# The root with path "/" should have a value of "#"
# API:

# get(path): String -> returns the value of a the node at the given path
# set(path, value) -> changes the value of a given node to the new value. Should error out if the path does not currently exist
# create(path, value) -> creates a new node and sets it to the given value. 
#Should error out if the node already exists or if the node’s parent does not exist. I.e. "/level1/level2" cannot be created if /level1 has not already been created.
# delete(path) -> deletes a node, but ONLY if it has no children
# Clarification:

# get(): a user can only retrieve value from an existing node in the path.
# set(): a user can only set the value on an existing node. Cannot set root's value.
# create(): a user can only create node one level deeper than the existing node.
# delete(): a user can only delete node without children. Cannot delete root.

class Trie:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.children = defaultdict(Trie)

class FileSystem:
    def __init__(self):
        self.root = Trie('', '#')
    
    def get(self, path):
        dirs = path.split('/')
        curr = self.root
        for key in dirs[1:]:
            if key not in curr.children:
                return None
            curr = curr.children[key]
        return curr.val
    
    def set(self, path, value):
        dirs = path.split('/')
        curr = self.root
        for key in dirs[1:]:
            if key not in curr.children:
                return False
            curr = curr.children[key]
        curr.val = value
        return True
    
    def create(self, path, value):
        curr = self.root
        dirs = path.split('/')
        for key in dirs[1:-1]:
            if key not in curr.children:
                return False
            curr = curr.children[key]
        if dirs[-1] in curr.children or not dirs[-1]:
            return False
        curr.children[dirs[-1]] = Trie(dirs[-1], value)
        return True
    
    def delete(self, path):
        curr = par = self.root
        dirs = path.split('/')
        for key in dirs[1:]:
            if key not in curr.children:
                return False
            par = curr
            curr = curr.children[key]
        if curr.children:
            return False
        del par.children[curr.key]
        return True

obj = FileSystem()
print(obj.create("/a/b/c", "C"))
print(obj.get("/nonexistent"))
print(obj.create("/a", "A"))
print(obj.create("/a/b", "B"))
print(obj.create("/a/b/c", "C"))
print(obj.delete("/a"))
print(obj.delete("/a/b"))
print(obj.get("/a"))
print(obj.get("/a/b"))
print(obj.get("/a/b/c"))
print(obj.delete("/a/b/c"))
print(obj.delete("/a/b"))
print(obj.delete("/a"))
print(obj.create("/a/b", "AB"))
print(obj.create("/a", "A"))
print(obj.get("/a"))
        