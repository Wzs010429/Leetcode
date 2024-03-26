# leetcode 406 根据身高重建队列

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []

        for i in range(len(people)):
            res.insert(people[i][1], people[i])

        return res
