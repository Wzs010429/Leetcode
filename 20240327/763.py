# leetcode 763 划分字母区间

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hashmap = dict()
        res = [-1]
        right = 0

        for i in range(len(s)):
            hashmap[s[i]] = i

        for i in range(len(s)):
            right = max(hashmap[s[i]], right)
            if i == right:
                res.append(i - sum(res))

        return res[1:]
