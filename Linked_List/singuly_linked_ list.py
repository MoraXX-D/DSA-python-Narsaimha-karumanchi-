class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def setData(self, data: any) -> None:
        self.data = data

    def getData(self) -> any:
        return self.data

    def setNext(self, next_node: 'Node') -> None:
        self.next = next_node

    def getNext(self) -> 'Node':
        return self.next

    def hasNext(self) -> bool:
        return self.next is not None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def insertAtBeginning(self, data: any) -> None:
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
        self.size += 1

    def insertAtEnd(self, data: any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)
        self.size += 1

    def insertInMiddle(self, position: int, data: any) -> None:
        if position > self.size or position < 0:
            raise IndexError("Position out of bounds")
        if position == 0:
            self.insertAtBeginning(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 1):
                current = current.getNext()
            new_node.setNext(current.getNext())
            current.setNext(new_node)
            self.size += 1

    def deleteFromBeginning(self) -> None:
        if self.size == 0:
            print("List is empty")
        else:
            self.head = self.head.getNext()
            self.size -= 1

    def deleteFromEnd(self) -> None:
        if self.size == 0:
            print("List is empty")
        else:
            current = self.head
            previous = None
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            if previous is None:
                self.head = None
            else:
                previous.setNext(None)
            self.size -= 1

    def deleteIntermediate(self, position: int) -> None:
        if self.size == 0:
            raise ValueError("List is empty")
        if position >= self.size or position < 0:
            raise IndexError("Position out of bounds")
        current = self.head
        previous = None
        for _ in range(position):
            previous = current
            current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.size -= 1

    def deleteValue(self, value: any) -> None:
        current = self.head
        previous = None
        while current is not None:
            if current.getData() == value:
                if previous is None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                self.size -= 1
                return
            previous = current
            current = current.getNext()
        print("Value not found in the list")

    def printList(self) -> None:
        current = self.head
        while current is not None:
            print(current.getData(), end=" -> ")
            current = current.getNext()
        print("None")


def main():
    sll = SinglyLinkedList()

    print("Inserting at the beginning:")
    sll.insertAtBeginning(10)
    sll.insertAtBeginning(20)
    sll.printList()

    print("Inserting at the end:")
    sll.insertAtEnd(30)
    sll.insertAtEnd(40)
    sll.printList()

    print("Inserting in the middle:")
    sll.insertInMiddle(2, 25)
    sll.printList()

    print("Deleting from the beginning:")
    sll.deleteFromBeginning()
    sll.printList()

    print("Deleting from the end:")
    sll.deleteFromEnd()
    sll.printList()

    print("Deleting in the middle:")
    sll.deleteIntermediate(1)
    sll.printList()

    print("Deleting a specific value:")
    sll.deleteValue(25)
    sll.printList()


if __name__ == "__main__":
    main()
