from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)          # 半开区间 [l, r)
        while l < r:
            mid = l + (r - l) // 2   # 防溢出写法
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid              # 目标在左半
            else:
                l = mid + 1          # 目标在右半，必须 +1
        return -1


# ---------- 验证 ----------
if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 5, 8]
    print(s.search(a, 5))   # 2
    print(s.search(a, 2))   # 1
    print(s.search(a, 1))   # 0
    print(s.search(a, 8))   # 3
    print(s.search(a, 4))   # -1
