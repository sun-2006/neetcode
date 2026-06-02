class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.s=[]
        for i in tokens:
            if i not in ["+","-","*","/"] :
                self.s.append(int(i))
            else:
                o1=self.s.pop()
                o2=self.s.pop()
                if i=="+":
                    self.s.append(o2+o1)
                elif i=="-":
                    self.s.append(o2-o1)
                elif i=="*":
                    self.s.append(o2*o1)
                else:
                    self.s.append(int(o2/o1))
        return self.s.pop()
        