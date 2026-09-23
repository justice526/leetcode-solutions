#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    // 最优解：一遍遍历哈希（先查后存，天然无自匹配问题）
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;   // 值 -> 下标
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];            // 我需要的"搭档"值
            if (seen.find(need) != seen.end()) {    // 搭档已在前面出现过
                res.push_back(seen[need]);          // 更早的下标在前
                res.push_back(i);
                return res;
            }
            seen[nums[i]] = i;                      // 否则记下当前 (值, 下标)
        }
        return res;
    }

    /*
    // 替代解：两遍遍历哈希（先全存，再查；需注意自匹配）
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mem;
        for (int i = 0; i < nums.size(); i++) mem[nums[i]] = i;
        for (int i = 0; i < nums.size(); i++) {
            int x = target - nums[i];
            if (mem.find(x) != mem.end() && mem[x] != i) {
                return {i, mem[x]};
            }
        }
        return {};
    }
    */
};
