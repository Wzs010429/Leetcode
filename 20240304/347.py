# leetcode 347 前K个高频元素

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numlist = dict()
        for i in nums:
            if i not in numlist:
                numlist[i] = numlist.get(i, 0) + 1
            else:
                numlist[i] += 1

        return self.top_k_keys(numlist, k)

    def top_k_keys(self, input_dict, k):

        # input_dict.items()返回一个字典项的视图，其中每个元素都是一个键值对，形式为(key, value)的元组。
        # sorted()函数用于对这些元组进行排序。sorted()函数的key参数接受一个函数，这个函数指定排序依据。在这个例子中，使用了一个lambda函数lambda x: x[1]，它告诉sorted()函数根据每个元组的第二个元素（即字典的值）进行排序。
        # reverse=True参数指示sorted()函数按照降序排列元素，确保列表的开始部分是值最大的元素。

        # 按字典的值排序，返回一个由元组组成的列表，元组第一个元素是键，第二个元素是值
        sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)
        # 取前k个元素的键
        top_k = [item[0] for item in sorted_items[:k]]
        return top_k