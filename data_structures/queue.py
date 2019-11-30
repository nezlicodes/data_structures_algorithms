class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def peek(self):
        return self.queue[0]

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

queue = Queue()
queue.enqueue(0)
queue.enqueue(0)
queue.enqueue(2)

print(queue.peek())