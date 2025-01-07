import queue

# creates a stack
stack = queue.LifoQueue()

# adds elements to the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# sum the last two numbers of the stack
last_two_sum = stack.get() + stack.get()
print("Sum of the last two numbers:", last_two_sum)

# calculate the sum of the remaining stack elements
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()

print("Sum of the remaining stack elements:", remaining_sum)