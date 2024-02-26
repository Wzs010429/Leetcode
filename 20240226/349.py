# Leetcode 349 两个数组的交集

# 双指针秒了


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 我还是喜欢用双指针来做
        # 首先为两个数组分别定义一个指针
        # 首先的首先是保证两个数组是从小到大的顺序的

        nums1.sort()
        nums2.sort()
        # 定义指针
        pointer1, pointer2 = 0, 0
        # 计算数组长度
        length1, length2 = len(nums1), len(nums2)

        # 定义输出数组
        ans = []
        flag = -1  # 定义前置加入的元素

        while pointer1 < length1 and pointer2 < length2:
            # 只有相等并且没在数组里面添加过才会被添加进去
            if nums1[pointer1] == nums2[pointer2] and nums1[pointer1] != flag:
                ans.append(nums1[pointer1])
                flag = nums1[pointer1]
                pointer1 += 1
                pointer2 += 1
            # 否则就是挪动指针
            elif nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1

        return ans



# 善用集合去做题

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 单纯给两个数组取集合之后，然后给求他们的交集 然后再转化成列表list
        return list(set(nums1) & set(nums2))


# 用哈希表去做
# 我说实话我觉得这个有点多余 但是就当练练手了
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 用哈希表去做 本质上是一个字典
        hashset = {}

        for i in nums1:
            hashset[i] = hashset.get(i, 0) + 1

        ans = set()

        for i in nums2:
            if i in hashset:
                ans.add(i)

        return list(ans)