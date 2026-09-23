from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                          # 值 -> 下标，哈希表
        for i, num in enumerate(nums):
            need = target - num            # 我需要的"搭档"值
            if need in seen:               # 搭档已经在前面出现过
                return [seen[need], i]     # 返回 [更早的下标, 当前下标]
            seen[num] = i                  # 否则把当前 (值, 下标) 记下来，供后面查
        return []                          # 题目保证有解，正常不会走到这里


# ---------- 验证（本地跑，提交时这段可留可删）----------
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))    # [0, 1]
    print(s.twoSum([3, 2, 4], 6))         # [1, 2]
    print(s.twoSum([3, 3], 6))            # [0, 1]
