#include <vector>
using namespace std;

class Solution {
public:
    // 二分查找（半开区间模板 [l, r)）
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();   // r 是"开"边界，不含
        while (r != l) {               // 区间非空
            int mid = l + (r - l) / 2; // 防溢出写法（等价于 (l+r)/2）
            if (nums[mid] == target) return mid;
            else if (nums[mid] > target) r = mid;   // 目标在左半：右边界收到 mid（开区间，mid 已排除）
            else l = mid + 1;                       // 目标在右半：左边界越过 mid（必须 +1，否则窗口=2 时死循环）
        }
        return -1;                     // 没找到
    }
};
