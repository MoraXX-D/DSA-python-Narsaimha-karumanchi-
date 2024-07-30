class Node:
    def __init__(self data = None, last = None) -> None:
        self.data = None
        self.last = None
        self.next = None
    
    def setData(self,data) -> None:
        self.data = data
        
    def getData(self) -> any:
        return self.data
    
    def setNext(self,next) -> None:
        self.next = next
        
    def getNext(self) -> 'Node':
        return self.next
    
    def setLast(self,last) -> None:
        self.last = last
        
    def getLast(self) -> 'Node':
        return self.last
    
    def hasNext(self) -> bool:
        return self.next is not None
    
class Queue(object):
    
    def __init__(self,data = None) -> None:
        self.front = None
        self.rear = None
        self.size = 0
        
    def enQueue(self,data: any) -> None:
        self.lastNode = self.front
        self.front = Node(data,self.front)
        if self.lastNode:
            self.lastNode.setLast(self.front)
    