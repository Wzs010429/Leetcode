# leetcode 135 分发糖果

class Solution:
    def candy(self, ratings: List[int]) -> int:

        result = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1]+1

        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i+1]+1, result[i])


        return sum(result)
