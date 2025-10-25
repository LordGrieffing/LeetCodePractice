class node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.cache = {}
        
        
        self.left = node(0, 0)
        self.right = node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    def add(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node 
        node.prev, node.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)