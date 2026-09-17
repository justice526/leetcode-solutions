# LC 387 字符串中的第一个唯一字符（Easy）
# 模型/套路：哈希计数 + 两遍扫描
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)                 # 统计频次（等价于手写 cnt[c] = cnt.get(c, 0) + 1）
        for i, c in enumerate(s):        # 按原顺序找第一个唯一字符
            if cnt[c] == 1:
                return i
        return -1                        # 没有唯一字符


# 自测
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))       # 0 ('l')
    print(sol.firstUniqChar("loveleetcode"))   # 2 ('v')
    print(sol.firstUniqChar("aabb"))           # -1
