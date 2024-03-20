# leetcode 332 重新安排行程


## 方法1 使用used数组 但是有一个测试案例超时了
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()  # 先排序，这样一旦找到第一个可行路径，一定是字母排序最小的
        used = [0] * len(tickets)
        path = ['JFK']
        results = []
        self.backtracking(tickets, used, path, 'JFK', results)
        return results[0]

    def backtracking(self, tickets, used, path, cur, results):
        if len(path) == len(tickets) + 1:  # 终止条件：路径长度等于机票数量+1
            results.append(path[:])  # 将当前路径添加到结果列表
            return True

        for i, ticket in enumerate(tickets):  # 遍历机票列表
            if ticket[0] == cur and used[i] == 0:  # 找到起始机场为cur且未使用过的机票
                used[i] = 1  # 标记该机票为已使用
                path.append(ticket[1])  # 将到达机场添加到路径中
                state = self.backtracking(tickets, used, path, ticket[1], results)  # 递归搜索
                path.pop()  # 回溯，移除最后添加的到达机场
                used[i] = 0  # 标记该机票为未使用
                if state:
                    return True  # 只要找到一个可行路径就返回，不继续搜索



# 字典

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = defaultdict(list)
        for ticket in tickets:
            targets[ticket[0]].append(ticket[1])
        for airport in targets.keys():
            targets[airport].sort()

        path = ["JFK"]
        self.backTracking(targets, path, len(tickets))
        return path

    def backTracking(self, targets, path, ticketNum):
        if len(path) == ticketNum + 1:
            return True

        airport = path[-1]
        destinations = targets[airport]

        for i, dest in enumerate(destinations):
            targets[airport].pop(i)  # 标记已使用的机票
            path.append(dest)  # 添加目的地到路径
            if self.backTracking(targets, path, ticketNum):
                return True  # 找到有效行程
            targets[airport].insert(i, dest)  # 回溯，恢复机票
            path.pop()  # 移除目的地
        return False  # 没有找到有效行程