# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        d = {}
        for idx, i in enumerate(indices):
            d.update({i:s[idx]})
            nStr = "" # new string

        for i in range(len(d)):
            nStr += d[i]
        return(nStr)
