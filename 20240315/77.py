# leetcode 77 组合


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        ## 首先是一个未剪枝的版本
        ## 定义两个全局变量数组
        result = []
        path = []
        self.backtracking(n, k, 1, result, path)

        return result
    
    def backtracking(self, n, k, starIndex, result, path):
        if len(path) == k:
            result.append(path[:]) ## 这块是为了避免传递引用
            return
        
        for i in range(starIndex, n+1):
            path.append(i)
            self.backtracking(n, k, i+1, result, path)
            path.pop()
    

# 剪枝优化


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点

