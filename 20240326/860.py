# leetcode 860 柠檬水找零

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        # 这道题目还是用贪心来做

        chargedict = dict()

        for i in bills:
            # 一共有三种情况　
            if i == 5:
                chargedict[i] = chargedict.get(i, 0) + 1

            if i == 10:
                if chargedict.get(5, 0) <= 0:
                    return False

                else:
                    chargedict[i] = chargedict.get(i, 0) + 1
                    chargedict[5] -= 1

            if i == 20:
                if chargedict.get(5, 0) > 0 and chargedict.get(10, 0) > 0:
                    chargedict[5] -= 1
                    chargedict[10] -= 1

                elif chargedict.get(5, 0) >= 3 and chargedict.get(10, 0) == 0:
                    chargedict[5] -= 3

                else:
                    return False

        return True
