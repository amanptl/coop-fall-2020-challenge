class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stack = []
        self.stack.append(self.value)
        self.pointer = -1

    def add(self, num: int):
        self.value += num
        self.stack.append(num * -1)

    def subtract(self, num: int):
        self.value -= num
        self.stack.append(num)

    def undo(self, steps = 1):
        if self.pointer < 0:
            self.pointer = len(self.stack)

        self.pointer -= 1
        self.pointer = max(self.pointer, 0)
        self.value += self.stack[self.pointer]
        print(self.value)
        
    def redo(self, steps = 1):
        if self.pointer < 0:
            self.pointer = len(self.stack) - 1
        if self.pointer == len(self.stack):
            return
        
        self.pointer += 1
        self.pointer = min(self.pointer, len(self.stack)-1)
        self.value += self.stack[self.pointer] * -1
        

    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()
