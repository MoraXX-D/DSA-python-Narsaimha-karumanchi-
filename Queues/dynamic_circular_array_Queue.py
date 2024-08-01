class Queue(object):
    def __init__(self, limit=5) -> None:
        self.que = [None] * limit
        self.limit = limit
        self.front = 0
        self.rear = -1
        self.size = 0

    def empty(self) -> bool:
        return self.size == 0

    def enQueue(self, data) -> None:
        if self.size >= self.limit:
            self.resize()

        self.rear = (self.rear + 1) % self.limit
        self.que[self.rear] = data
        self.size += 1

        print("Queue after enQueue", self.que)

    def deQueue(self):
        if self.size <= 0:
            print('Queue Underflow')
            return

        self.que[self.front] = None
        self.front = (self.front + 1) % self.limit
        self.size -= 1

        if self.size == 0:
            self.front = 0
            self.rear = -1

        print("Queue after deQueue", self.que)

    def queRear(self):
        if self.empty():
            print("Sorry, the Queue is empty")
            raise IndexError

        return self.que[self.rear]

    def queFront(self):
        if self.empty():
            print("Sorry, the Queue is empty")
            raise IndexError

        return self.que[self.front]

    def queueSize(self):
        return self.size

    def resize(self):
        new_limit = 2 * self.limit
        new_que = [None] * new_limit

        for i in range(self.size):
            new_que[i] = self.que[(self.front + i) % self.limit]

        self.que = new_que
        self.front = 0
        self.rear = self.size - 1
        self.limit = new_limit

        print("Queue resized to", self.limit)

# Example usage
que = Queue()
que.enQueue('first')
print("Front:", que.queFront())
print("Rear:", que.queRear())
que.enQueue('second')
print("Front:", que.queFront())
print("Rear:", que.queRear())
que.enQueue('third')
print("Front:", que.queFront())
print("Rear:", que.queRear())
que.enQueue('fourth')
print("Front:", que.queFront())
print("Rear:", que.queRear())
que.enQueue('Fifth')
print("Front:", que.queFront())
print("Rear:", que.queRear())
que.enQueue('Sixth')
print("Front:", que.queFront())
print("Rear:", que.queRear())
que.deQueue()
print("Front:", que.queFront())
print("Rear:", que.queRear())
que.deQueue()
print("Front:", que.queFront())
print("Rear:", que.queRear())
