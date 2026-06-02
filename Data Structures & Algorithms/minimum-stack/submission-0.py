class MinStack:

    def __init__(self):
        self.s=[]
        self.s1=[]

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.s1:
            val=min(self.s1[-1],val)
        self.s1.append(val)
    def pop(self) -> None:
        self.s.pop()
        self.s1.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s1[-1]
