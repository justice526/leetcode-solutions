// LC 1751 最多可以参加的会议数目 II (Hard)
// 带权区间调度 + 最多选 k 个：按结束时间排序 + 二分找前驱 + 二维 DP
// 关键点：本题“结束日 inclusive，同一天不能既结束又开始” → 严格不重叠 → 用 lower_bound
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        int n = events.size();

        // 1) 拆成 (结束时间, 开始时间, 价值)，按结束时间升序排序
        vector<tuple<int, int, int>> meeting;
        for (int i = 0; i < n; i++) {
            int l = events[i][0];   // 开始
            int r = events[i][1];   // 结束
            int w = events[i][2];   // 价值
            meeting.emplace_back(r, l, w);
        }
        sort(meeting.begin(), meeting.end());

        // 2) 抽出有序的结束时间数组，供二分找“前驱”
        vector<int> ends;
        for (auto& x : meeting) ends.push_back(get<0>(x));

        // 3) dp[i][j] = 前 i 个会议中，最多选 j 个能获得的最大价值
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
        for (int i = 0; i < n; i++) {
            auto [r, l, w] = meeting[i];
            // p = “结束时间 < 当前开始时间”的会议个数
            //    严格小于！因为 end == start 也算冲突（lower_bound / bisect_left）
            int p = lower_bound(ends.begin(), ends.end(), l) - ends.begin();
            for (int j = 1; j <= k; j++) {
                // 不选第 i 个：dp[i][j]
                // 选第 i 个  ：dp[p][j-1] + w（用掉一个名额，故第二维 -1）
                dp[i + 1][j] = max(dp[p][j - 1] + w, dp[i][j]);
            }
        }
        return dp[n][k];
    }
};
