class Node:
    def __init__(self , key , val):
        self.key = key
        self.val = val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict(int) # key - LL pointing to node
        self.left , self.right = Node(0 , 0) , Node(0 , 0)
        self.left.nxt , self.right.prev = self.right , self.left
        # self.left - lru , self.right = mru

    def remove(self , node):
        # delete from the left
        pre , nex = node.prev , node.nxt
        pre.nxt = nex
        nex.prev = pre
    def add(self , node):
        # add to the right
        pre , nxt = self.right.prev , self.right
        pre.nxt = node
        node.prev = pre
        node.nxt = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        # make the key the most recently used key

        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key , value)
        self.add(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.cap:
            # delete lru
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

