# LC 1477 找两个和为目标值且不重叠的子数组（Medium）
# 模型/套路：全正数 → 滑动窗口；两个不重叠最优配对 → 前缀最优 best
class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')
        best = [INF] * n          # best[i] = arr[0..i] 内和为 target 的最短子数组长度
        ans = INF
        s = 0                     # 滑动窗口 [l..r] 的和
        l = 0
        for r in range(n):
            s += arr[r]
            while s > target:     # 全正数：和超了就缩左端
                s -= arr[l]
                l += 1
            if r > 0:
                best[r] = best[r - 1]              # ① 继承前缀最优（记账）
            if s == target:
                length = r - l + 1
                best[r] = min(best[r], length)     # ② 用当前窗口刷新前缀最优
                if l > 0 and best[l - 1] != INF:   # ③ 查账：搭档必须完全在 l 左边
                    ans = min(ans, best[l - 1] + length)
        return -1 if ans == INF else ans


# 自测
if __name__ == "__main__":
    sol = Solution()
    print(sol.minSumOfLengths([3, 2, 2, 4, 3], 3))           # 2
    print(sol.minSumOfLengths([7, 3, 4, 7], 7))              # 2
    print(sol.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6))     # -1
