class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else: # Customer gives $20
                # Strategy: Try giving $10 + $5 first, then three $5s
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
                    
        return True
