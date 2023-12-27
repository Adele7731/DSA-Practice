class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        """Add an element to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the first item in the queue"""
        if len(self.items) != 0:
            self.items.pop(0)
        return f"List is empty"