class MyQueue:

    # Constructor 
    # Stack 1 is used for all pushing operations
    # Stack 1 is used to append to the front of the queue
    # Stack 2 is used for all popping operations
    # Stack 2 is used to pop from the front of the queue
    def __init__(self):
        self.s1 = []
        self.s2 = []        

    # Pushing all items onto stack 1
    # Appending all items to the queu
    def push(self, x: int) -> None:
        self.s1.append(x)
        
    # To pop from queue use stack 2
    # Check if stack 2 is empty
    # If stack 2 is empty then pop all things off stack 1
    # Popping all elements starting from the end of stack 1 puts them in reverse order in stack 2
    # Stack 1 = [1, 2, 3, 4] Stack 2 (after pushing) = [4, 3, 2, 1]
    # By pushing everything onto stack 2, the elements are in reverse
    # Now when you pop from stack 2 (stacks pop rightmost element)
    # The front of the queue is popped off
    # So if stack 2 is empty then pop everything off stack 1 and append it to stack 2
    # This puts all elements of stack 1 in reverse order when they are appended to stack 2
    # Once everything is pushed onto stack 2, then popping, pops off the last element in stack 2
    # Last element in stack 2 is the first element in stack 1 and first element in queue
    # When s2 is not empty then the first element in the queue is in stack 2
    # Thus we simply pop when stack 2 is not empty
    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    # Does the same thing as pop, has the same logic
    # But returns the value at the front of the queue (first element of stack 1, last element of stack 2)
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    # Return true if the biggest length of a stack is 0
    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()