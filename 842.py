class Solution:
    
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.ansList = list ()
        L = len(num)
        for i in range (1,int(L+1/3)):
            for j in range(1,L-i):
                a0  = num[:i]
                a1  = num[i:i+j]
                res = self.isFib(num[i+j:],a0,a1)
                if res!= False:
                    return [a0,a1]+self.ansList
    
    def invalidFomrat(self, string):
        if len(string)>1 and string[0]=='0':
            return True
    
    def isFib(self, number, a0, a1):
        if self.invalidFomrat(a0) or self.invalidFomrat(a1):
            return False
        sum_ = int(a0)+int(a1)
        k = len(str(sum_)) #number of digits of sum_
        if k>10 :
            return False
        if k==10 and str(sum_)>"2147483647":
            return False
        a2 = number[:k]
        if int(a2)==sum_:
            self.ansList.append(a2)
            newNumber = number[k:]
            if len(newNumber)>0:
                return self.isFib(newNumber, a1, a2)
            else:
                return True
        else:
            if len(self.ansList)>0:
                self.ansList.pop()
            return False