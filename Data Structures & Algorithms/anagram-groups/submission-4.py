class Solution:
    def anagrams(self,data1: str,data2: str):
        if(len(data1)!=len(data2)):
            return False
        return sorted(data1)==sorted(data2)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {''.join(sorted(i)): [] for i in strs}
        l1=[]
        for i in strs:
            dict1[''.join(sorted(i))].append(i)
        for key,value in dict1.items():
            l1.append(value)
        return l1
        