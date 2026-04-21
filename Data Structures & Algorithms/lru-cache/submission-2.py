class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        #init capacity
        self.cap = capacity
        #hash map. key : node(key, val)
        self.cache = {}
        #keep track of lru and mru with sentenial pointers 
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

        #linked list? 
        """
        put -> insert node at the front of linked list,
        update -> remove from current pos then insert at the front of the list
        over cap - > remove from the head of the list 
        """ 
    def remove(self, node):
        # store the curr nodes prev and next nodes
        pre, nxt = node.prev, node.next
        # set its prev to point at its next and its next to point at its prev
        pre.next, nxt.prev = nxt, pre

    def insert(self, node):
        # store current tail of the list
        pre = self.right.prev
        #set the tails next and the sentenials prev to node
        pre.next = self.right.prev = node
        #set nodes prev and next pointers
        node.prev, node.next = pre, self.right

    def get(self, key: int) -> int:
        #return value of key if it exists else -1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key exists update its value
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        # else add the key value pair to the cache
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
        # if adding a key goes over capacity then we need to remove the lru key
