class Queue(object):
    def __init__(self, limit=5) -> None:
        self.que = []
        self.limit = limit
        self.front = 0
        self.rear = -1
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def enQueue(self, data: any) -> 'Queue':
        if self.size >= self.limit:
            raise ValueError("Overflow")
        else:
            self.que.append(data)
            self.rear = self.size
            self.size += 1
            print('Queue after enQueue:', self.que)

    def deQueue(self) -> 'Queue':
        if self.isEmpty():
            raise ValueError("Underflow")
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = 0
                self.rear = -1
            else:
                self.rear = self.size - 1
            print("Queue after deQueue:", self.que)

    def queueRear(self) -> any:
        if self.isEmpty():
            print("Sorry, the queue is empty")
            raise IndexError("Rear not available")
        return self.que[self.rear]

    def queueFront(self) -> any:
        if self.isEmpty():
            print("Sorry, the queue is empty")
            raise IndexError("Front not available")
        return self.que[self.front]

    def queueSize(self) -> int:
        return self.size


# Example usage
que = Queue()
que.enQueue('first')
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
que.enQueue('second')
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
que.enQueue('third')
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
que.deQueue()
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
que.deQueue()
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
