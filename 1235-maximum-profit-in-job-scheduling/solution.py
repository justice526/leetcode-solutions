from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 按「结束时间」升序排序：zip(end, start, profit) 让 endTime 排在第一位
        jobs = sorted(zip(endTime, startTime, profit))
        ends = [j[0] for j in jobs]          # 所有区间的结束时间（已升序）
        n = len(startTime)

        # dp[i] = 前 i 个区间（按结束时间排）能拿到的最大收益；dp[0] = 0 哨兵
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            r, l, w = jobs[i - 1]            # 当前区间（0 基取第 i-1 个）
            # 找「最后一个结束时间 <= 当前开始时间」的区间（背靠背不算重叠 → bisect_right）
            p = bisect_right(ends, l) - 1
            # 选当前区间：只能叠在不重叠的前驱上；p 是 0 基下标，套进 1 基 dp 要 +1
            take = w + dp[p + 1]
            # 不选当前区间则继承 dp[i-1]；两条路取大
            dp[i] = max(dp[i - 1], take)

        return dp[n]
