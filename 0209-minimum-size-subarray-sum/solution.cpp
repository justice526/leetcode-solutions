#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = 0;
        int total = 0;
        int ans = INT_MAX;          // 最小长度，初始无穷大

        while (right < n) {
            total += nums[right];   // 右扩：纳入 nums[right]
            right++;
            // 左缩：窗口和达标就尽量缩 left，得到以 right 结尾的最短合法窗口
            while (total >= target) {
                ans = min(ans, right - left);   // 最短 → 取最小；更新到 ans 自身
                total -= nums[left];
                left++;
            }
        }
        return ans == INT_MAX ? 0 : ans;        // 没找到合法窗口返回 0
    }
};
