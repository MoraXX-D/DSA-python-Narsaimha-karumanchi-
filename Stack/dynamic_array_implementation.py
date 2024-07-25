class Stack(object):
    def __init__(self, limit = 10) -> None:
        self.stk = limit*[]
        self.limit = limit
        
    def isEmpty(self):
        return len(self.stk) <= 0
    
    def push(self, item: any) -> None:
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print(f"Stack after push: {self.stk}")
    
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None
        else:
            return self.stk.pop()
        
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None
        else:
            return self.stk[-1]
    
    def size(self):
        return len(self.stk)
    
    def resize(self):
        newStk =list(self.stk)
        self.limit = 2*self.limit
        self.stk = newStk
# Example usage
our_stack = Stack(5)
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("31")
our_stack.push("19")
our_stack.push("3")  # Doubling happened 
our_stack.push("99")  
our_stack.push("9")  

print(our_stack.peek())  # Should print the top element
print(our_stack.pop())   # Should remove and print the top element
print(our_stack.peek())  # Should print the new top element after pop
print(our_stack.pop())   # Should remove and print the new top element