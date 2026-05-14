class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity

        self.cache = {} # key -> node

        self.left, self.right = Node(0, 0), Node(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt
       
    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
        node.next = node.prev = None

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 
        

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            if self.capacity == len(self.cache):
                lru = self.left.next
                self.remove(lru)
                self.cache.pop(lru.key)
                
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])




