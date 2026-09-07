class LL:
    def __init__(self, val=(-1, -1), prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.life_head = LL()   # dummy LRU side
        self.life_tail = LL()   # dummy MRU side

        self.life_head.next = self.life_tail
        self.life_tail.prev = self.life_head


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            node.prev.next = node.next
            node.next.prev = node.prev

            prev_node = self.life_tail.prev
            prev_node.next = node
            node.prev = prev_node
            node.next = self.life_tail
            self.life_tail.prev = node

            return node.val[1]

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.val = (key, value)

            prev_node = self.life_tail.prev
            prev_node.next = node
            node.prev = prev_node
            node.next = self.life_tail
            self.life_tail.prev = node

            return

        new_node = LL((key, value))

        prev_node = self.life_tail.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.life_tail
        self.life_tail.prev = new_node

        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            old_node = self.life_head.next

            self.life_head.next = old_node.next
            old_node.next.prev = self.life_head

            self.cache.pop(old_node.val[0])

