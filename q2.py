from collections import deque


class CircularBufferList:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self.size == self.capacity:
            raise Exception("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def __str__(self):
        return str(self.buffer)


class CircularBufferDeque:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def enqueue(self, item):
        if len(self.buffer) == self.buffer.maxlen:
            raise Exception("Buffer is full")
        self.buffer.append(item)

    def dequeue(self):
        if not self.buffer:
            raise Exception("Buffer is empty")
        return self.buffer.popleft()

    def __str__(self):
        return str(self.buffer)
