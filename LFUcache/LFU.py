class node:

    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq

        self.prev = None
        self.next = None

    def upFreq(self):
        self.freq += 1

class LinkedList:

    def __init__(self, freq):
        self.freq = freq

        self.right = node(0,0,freq)
        self.left = node(0,0,freq)

        self.right.prev = self.left
        self.left.next = self.right

        self.length = 0

    def add(self, node):
        node.next, node.prev = self.right, self.right.prev

        prv , nxt = self.right.prev, self.right
        prv.next = nxt.prev = node

        self.length += 1

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

        self.length -= 1


class LFUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.cache = {}
        self.freqCache = {}
        self.LFUcount = 0


    def get(self, key: int) -> int:

        if key in self.cache:
            cnt = self.cache[key].freq
            self.freqCache[cnt].remove(self.cache[key])

            # Check if new freq exist
            if cnt + 1 not in self.freqCache:
                self.freqCache[cnt + 1] = LinkedList(cnt+1)

            # Remove empty list
            if self.freqCache[cnt].length < 1:
                del self.freqCache[cnt]
                
                if self.LFUcount == cnt:
                    self.LFUcount = cnt + 1

            
            self.freqCache[cnt + 1].add(self.cache[key])
            self.cache[key].upFreq()
            return self.cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:

        if self.cap == 0:
            return
        
        if key in self.cache:
            cnt = self.cache[key].freq
            self.cache[key].val = value
            self.freqCache[cnt].remove(self.cache[key])

            # Check if new freq exist
            if cnt + 1 not in self.freqCache:
                self.freqCache[cnt + 1] = LinkedList(cnt+1)

            self.freqCache[cnt + 1].add(self.cache[key])
            self.cache[key].upFreq()

            # Remove empty list
            if self.freqCache[cnt].length < 1:
                del self.freqCache[cnt]
                
                if self.LFUcount == cnt:
                    self.LFUcount = cnt + 1

        else:

            if len(self.cache) == self.cap:
                LRU_LFU = self.freqCache[self.LFUcount].left.next
                self.freqCache[self.LFUcount].remove(LRU_LFU)
                del self.cache[LRU_LFU.key]

                # Remove empty list
                if self.freqCache[self.LFUcount].length < 1:
                    del self.freqCache[self.LFUcount]
                    self.LFUcount += 1
            
            self.cache[key] = node(key, value, 1)
            
            if 1 not in self.freqCache:
                self.freqCache[1] = LinkedList(1)

            self.freqCache[1].add(self.cache[key])
            self.LFUcount = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)