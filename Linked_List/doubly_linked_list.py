class Node:
    
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
        self.prev = None
        
        
    def setData(self, data: any) -> None:
        self.data = data
        
    def getData(self) -> any:
        return self.data
    
    def setNext(self,next_node: 'Node') -> None:
        self.next = next_node
        
    def getNext(self) -> 'Node':
        return self.next

    def hasNext(self) -> bool:
        return self.next is not None
    
    def setPrev(self,prev_node: 'Node') -> None:
        self.prev = prev_node
        
    def getPrev(self) -> 'Node':
        return self.prev
    
    def hasPrev(self) -> bool:
        return self.prev != None
    
    def __str__(self) -> str:
        return f"Node[Data = {self.data}]"
    
class DoublyLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        
    def insertAtBeginning(self,data: any) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        self.size += 1
            
    def insertAtEnd(self,data: any) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.getNext() is not None:
                currentNode = currentNode.getNext()
            currentNode.setNext(newNode)
            newNode.setPrev(currentNode)
        self.size += 1
            
    def insertInMiddle(self, data: any, position: int) -> None:
        if position <= 0 or position > self.size + 1:
            raise ValueError("Position out of bounds") 
        
        if position == 1:
            self.insertAtBeginning(data)
            return
        
        if position == self.size + 1:
            self.insertAtEnd(data)
            return
        
        newNode = Node(data)
        currentNode = self.head
        for _ in range(position - 2):
            currentNode = currentNode.getNext()
        
        newNode.setNext(currentNode.getNext())
        newNode.setPrev(currentNode)
        currentNode.getNext().setPrev(newNode)
        currentNode.setNext(newNode)
        self.size += 1
                
    def display(self) -> 'DoublyLinkedList':
        if self.head is None:
            print("list is empty")
            return
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.getData(), end = " -> ")
                currentNode = currentNode.getNext()
            print("None")
            
    def deleteFromBeginning(self):
        if self.head is None:
            print("List is Empty")
            return
        
        elif self.head.getNext() is None:
            self.head = None
        
        else:
            self.head = self.head.getNext()
            self.head.setPrev(None)
            
        self.size -= 1
            
    def deleteFromEnd(self):
        if self.head is None:
            raise ValueError("List is empty")
        
        elif self.head.getNext() is None:
            self.head = None 
        else:
            currentNode = self.head
            while currentNode.getNext() is not None:
                currentNode = currentNode.getNext()
                
            currentNode.getPrev().setNext(None)
        self.size -= 1
            
    def deleteFromPosition(self,position):
        
        if self.head is None:
            raise ValueError("list is empty")
        
        if position <= 0 or position > self.size:
            raise ValueError("Position is out of bound")
        
        elif position == 1:
            self.deleteFromBeginning()
            return
        
        currentNode = self.head
        for _ in range(position - 1):
            currentNode = currentNode.getNext()
        
        if currentNode is None:
            print("position is greater then the size of the list")
            return
        
        elif currentNode.getNext() is None:
            currentNode.getPrev().setNext(None)
        
        else:
            currentNode.getPrev().setNext(currentNode.getNext())
            currentNode.getNext().setPrev(currentNode.getPrev())
            
            
        self.size -= 1
            
            
                
def main():
    
    dll = DoublyLinkedList()
    
    print("Inserting in the Beginning")
    dll.insertAtBeginning(20)
    dll.insertAtBeginning(10)
    
    
    print("Inserting in the End")
    dll.insertAtEnd(50)
    dll.insertAtEnd(60)
    
    
    print("Inserting in the Middle")
    dll.insertInMiddle(30,2)
    dll.insertInMiddle(40,3)
    
    dll.display()
    
    print("deleting from beginning")
    dll.deleteFromBeginning()
    
    print("deleting from end")
    dll.deleteFromEnd()
    
    print("deleting from middle")
    dll.deleteFromPosition(2)
    dll.deleteFromPosition(3)
                
    dll.display()
                
if __name__ == '__main__':
    main()
                
                
                
        
        
            
        
            
        
            
        
        
        
        
        
    
    
    