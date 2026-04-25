# node class 
    # store prev, next, val 
class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val
        self.prev = self.next = None

class LRUCache:
    """
    keep track of cached items within capacity 
    have a way to order the cache to know what the least and most recently used are
    get and put operations make a key most recently used 

    key value pairs make me think of a map 
    """

    def __init__(self, capacity: int):
        # init capacity
        self.cap = capacity

        # init cache map, key : node 
        self.cache = {}

        # left and right sentenial nodes for lru and mru
        self.left = self.right = Node(0,0)

        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # update prev->next to curr->next and next->prev to curr->prev
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.next = node.prev = None

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        # if key in map
        if key in self.cache:
            # update the cache order in constant time 
            # an array/list wont work because you would have to shift elements
            # maybe a doubly linked list? 
            # remove the cache[key] from linked list
            self.remove(self.cache[key])
            # re-add it to keep it at the front 
            self.insert(self.cache[key])
            # return cache[key]
            return self.cache[key].val
        # return - 1
        return -1

    def put(self, key: int, value: int) -> None:
        # if key in cache:
        if key in self.cache:
            # cache[key].val = value
            self.cache[key].val = value
            # remove the cache[key] from linked list
            self.remove(self.cache[key])
            # re-add it to keep it at the front 
            self.insert(self.cache[key])
        # else:
        else:
            # cache[key] = node(key, val)
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insert(newNode)
        
        # if len(cache) > cap:
        if len(self.cache) > self.cap:
            # remove lru
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
        
