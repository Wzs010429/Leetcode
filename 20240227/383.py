# leetcode 383 赎金信 easy

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # 简单题 秒了 就是两个哈希表数值比对
        numRansomNote = dict()
        numMagazine = dict()

        for i in ransomNote:
            numRansomNote[i] = numRansomNote.get(i, 0) + 1

        for i in magazine:
            numMagazine[i] = numMagazine.get(i, 0) + 1

        # 比较 ransomNote的值都比magazine小就好了

        for i in numRansomNote:
            if i in numMagazine and numRansomNote[i] <= numMagazine[i]:
                continue
            else:
                return False

        return True
