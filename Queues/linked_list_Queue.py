class Node:
    def __init__(self, data=None, last=None) -> None:
        self.data = data
        self.last = last
        self.next = None

    def setData(self, data) -> None:
        self.data = data

    def getData(self) -> any:
        return self.data

    def setNext(self, next) -> None:
        self.next = next

    def getNext(self) -> 'Node':
        return self.next

    def setLast(self, last) -> None:
        self.last = last

    def getLast(self) -> 'Node':
        return self.last

    def hasNext(self) -> bool:
        return self.next is not None

class Queue(object):
    def __init__(self, data=None) -> None:
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data: any) -> None:
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.setNext(newNode)
            newNode.setLast(self.rear)
            self.rear = newNode
        self.size += 1

    def queueRear(self):
        if self.rear is None:
            print("Sorry, the queue is empty")
            raise IndexError
        return self.rear.getData()

    def queueFront(self):
        if self.front is None:
            print("Sorry, the queue is empty")
            raise IndexError
        return self.front.getData()

    def deQueue(self):
        if self.front is None:
            print("Sorry, the queue is empty")
            raise IndexError
        result = self.front.getData()
        self.front = self.front.getNext()
        if self.front is None:
            self.rear = None
        else:
            self.front.setLast(None)
        self.size -= 1
        return result

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
que.enQueue('fourth')
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
que.enQueue('Fifth')
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
que.enQueue('Sixth')
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
que.deQueue()
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
que.deQueue()
print("Front:", que.queueFront())
print("Rear:", que.queueRear())
