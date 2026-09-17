// LC 1477 找两个和为目标值且不重叠的子数组（Medium）
// 模型/套路：全正数 → 滑动窗口；两个不重叠最优配对 → 前缀最优 best
#include <vector>
#include <climits>     // INT_MAX
#include <algorithm>   // min
using namespace std;

class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        const int INF = INT_MAX;
        vector<int> best(n, INF);   // best[i] = arr[0..i] 内和为 target 的最短子数组长度
        int sum = 0, l = 0, res = INF;
        for (int r = 0; r < n; r++) {
            sum += arr[r];
            while (sum > target) sum -= arr[l++];   // 全正数：和超了就缩左端
            if (r > 0) best[r] = best[r - 1];       // ① 继承前缀最优（记账）
            if (sum == target) {
                int len = r - l + 1;
                best[r] = min(best[r], len);        // ② 用当前窗口刷新前缀最优
                if (l > 0 && best[l - 1] != INF)    // ③ 查账：搭档必须完全在 l 左边
                    res = min(res, best[l - 1] + len);
            }
        }
        return res == INF ? -1 : res;
    }
};
