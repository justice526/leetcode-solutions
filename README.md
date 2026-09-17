# leetcode-solutions

我的 LeetCode 题解仓库（Python + C++），按「模型 → 套路」学习法整理。
每题一个文件夹，内含代码 + README（题目 / 思路 / 复杂度 / 一题三问）。

## 进度

| 题号 | 题名 | 难度 | 模型 / 套路 | 语言 | 日期 |
|---|---|---|---|---|---|
| [387](./0387-first-unique-character-in-a-string) | 字符串中的第一个唯一字符 | Easy | 哈希计数 + 两遍扫描 | Python | 2026-09-17 |
| [1477](./1477-find-two-non-overlapping-sub-arrays-each-with-target-sum) | 找两个和为目标值且不重叠的子数组 | Medium | 滑动窗口 + 前缀最优 best | Python / C++ | 2026-09-17 |

> 待回填：LC 1235 规划兼职工作（带权区间调度地基）

## 目录结构
```
leetcode-solutions/
├── 0387-first-unique-character-in-a-string/
│   ├── README.md
│   └── solution.py
└── 1477-find-two-non-overlapping-sub-arrays-each-with-target-sum/
    ├── README.md
    ├── solution.py
    └── solution.cpp
```

## 使用说明
- 每日 AC 后新建 `题号-英文slug/` 文件夹，内含 `README.md` + `solution.*`。
- 提交：`git add . && git commit -m "LC xxxx" && git push`
