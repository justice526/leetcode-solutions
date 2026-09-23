from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口（数组全为正数 → 右扩和增、左缩和减，单调性保证 O(n)）
        n = len(nums)
        left = right = 0          # 窗口 [left, right)
        total = 0                 # 窗口内元素和
        ans = float('inf')        # 记录最小长度，初始无穷大

        while right < n:
            total += nums[right]  # 右扩：纳入 nums[right]
            right += 1
            # 左缩：只要窗口和达标就尽量往右缩 left，得到以 right 结尾的最短合法窗口
            while total >= target:
                ans = min(ans, right - left)   # 最短 → 取最小；更新到 ans 自身
                total -= nums[left]
                left += 1

        # 找不到任何合法窗口时 ans 仍为无穷大，返回 0
        return 0 if ans == float('inf') else ans
