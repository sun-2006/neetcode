class Solution:
    def calPoints(self, operations: List[str]) -> int:
        k=0
        l1=list()
        while k<len(operations):
            if operations[k].isdigit() or '-' in operations[k]:
                l1.append(int(operations[k]))
            elif operations[k]=='+':
                l1.append(l1[-1]+l1[-2])
            elif operations[k]=='D':
                l1.append(2*l1[-1])
            elif operations[k]=='C':
                l1.pop()

            k+=1
        print(l1)
        return sum(l1)

            


        