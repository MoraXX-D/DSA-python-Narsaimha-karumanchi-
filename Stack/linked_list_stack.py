class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
    
    def setData(self,data) -> None:
        self.data = data
        
    def getData(self) -> any:
        return self.data
    
    def setNext(self,next) -> None:
        self.next = next
        
    def getNext(self) -> 'Node':
        return self.next
    
    def hasNext(self) -> bool:
        return self.next is not None
    
    
class Stack(object):
        
    def __init__(self,data = None) -> None:
        self.head = None
        if data:
            for data in data:
                self.push(data)
        
    def push(self,data) -> None:
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp
            
    def pop(self) -> any:
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp
        
    def peek(self) -> any:
        if self.head is None:
            raise IndexError
        return self.head.getData()
        
        
our_list = ['apple','banana','avocado','oranges','pear']
our_stack = Stack(our_list)
print(our_stack.pop())
print(our_stack.pop())   
our_stack.push('mango')
print(our_stack.peek())      
        
        