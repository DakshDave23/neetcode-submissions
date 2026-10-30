class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        for i,stri in enumerate(strs):
            hashset[stri] = i
        ans = []
        ansidx = []
        temp = []
        trackeridx = [0]*len(strs)
        for i in range(len(strs)):
            lst = [c for c in strs[i]]
            lst.sort()
            tempstr = ''
            for j in lst:
                tempstr+=j
            trackeridx[i] = [tempstr,i]
        trackeridx.sort()
        temp.append(trackeridx[0][1])
        for i in range(1,len(strs)):
            if trackeridx[i][0] == trackeridx[i-1][0]:
                temp.append(trackeridx[i][1])
            else:
                ansidx.append(temp)
                temp = [trackeridx[i][1]]
        ansidx.append(temp)
        
        for i in range(len(ansidx)):
            temp = []
            for j in range(len(ansidx[i])):
                temp.append(strs[ansidx[i][j]])
            ans.append(temp)
        return ans

        