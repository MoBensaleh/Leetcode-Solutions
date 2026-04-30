class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.map = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_front(self, node): 
        current_first = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = current_first
        current_first.prev = node
    
    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node.prev = None
        node.next = None
    
    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)
    
    def _remove_lru(self):
        lru_node = self.tail.prev

        self._remove_node(lru_node)

        return lru_node

        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_front(node)
            return
        if len(self.map) == self.capacity:
            lru_node = self._remove_lru()
            del self.map[lru_node.key]
        
        new_node = Node(key, value)
        self._add_to_front(new_node)
        self.map[key] = new_node
