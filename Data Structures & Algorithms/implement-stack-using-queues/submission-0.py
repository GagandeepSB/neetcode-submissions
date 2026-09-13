class MyStack:

    # This is the constructor
    def __init__(self):
        # Initializing the queue (using deque)
        self.q = deque()
        
    # Pushing things onto our queue 
    # This appends the element to the right side of the queue
    def push(self, x: int) -> None:
        self.q.append(x)

    # In a stack values are only removed from the right side (aka top)
    # Can only remove from the left in a queue
    # Loop over all elements in the queue except the last one
    # In the loop pop every value except the last one
    # self.push adds the value back to the right side of the queue
    # Loop ends once we reach the last element
    # Last element is the element we want to pop
    # We pop the last element (since now it's at the fron of the queue)
    # Pop left element and return the value of that element 
    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    # Returning the top value (the most recently added value)
    def top(self) -> int:
        return self.q[-1]

    # return True if len of queue is 0
    # otherwise return False
    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()