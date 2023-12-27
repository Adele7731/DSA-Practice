class Node:
    data = None
    next_node = None


    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Node: {self.data}"


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Return True if the list is empty."""
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = self.next_node
        return count
        






n1 = Node(10)
print(n1)
print(f"Next node of n1 is :{n1.next_node}")

n2 = Node(20)

n1.next_node = n2

print(f"Next node of n1 is :{n1.next_node}")