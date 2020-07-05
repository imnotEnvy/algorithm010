本周作业
简单：
- [x] 柠檬水找零（亚马逊在半年内面试中考过）
- [x] 买卖股票的最佳时机 II （亚马逊、字节跳动、微软在半年内面试中考过）
- [x] 分发饼干（亚马逊在半年内面试中考过）
- [x] 模拟行走机器人
- [x] 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
说明：同学们可以将自己的思路、代码写在第 4 周的学习总结中
中等：
- [x] 单词接龙（亚马逊在半年内面试常考）
- [x] 岛屿数量（近半年内，亚马逊在面试中考查此题达到 350 次）
- [ ] 扫雷游戏（亚马逊、Facebook 在半年内面试中考过）
- [ ] 跳跃游戏 （亚马逊、华为、Facebook 在半年内面试中考过）
- [x] 搜索旋转排序数组（Facebook、字节跳动、亚马逊在半年内面试常考）
- [ ] 搜索二维矩阵（亚马逊、微软、Facebook 在半年内面试中考过）
- [ ] 寻找旋转排序数组中的最小值（亚马逊、微软、字节跳动在半年内面试中考过）
困难
- [x] 单词接龙 II （微软、亚马逊、Facebook 在半年内面试中考过）
- [ ] 跳跃游戏 II （亚马逊、华为、字节跳动在半年内面试中考过）


# 柠檬水找零

```python3
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five, ten = 0, 0

        for bill in bills:

            if bill == 5:
                five += 1

            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False

            elif bill == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif ten == 0 and five > 3:
                    five -= 3
                else:
                    return False
        return True
```

# 买卖股票的最佳时机 II

```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit
```

# 分发饼干

```python3
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        if (len(s) == 0) or (len(g) == 0) or (s[-1] < g[0]):
            return 0

        i, j, satisfied = 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                satisfied += 1
                s[j] = 0
                i += 1
            j += 1
        return satisfied
```

# 模拟行走机器人

复数法代码比较简单

```python3
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans, p, q = 0, 0, 1j
        obstacles = {complex(*it) for it in obstacles}

        for c in commands:
            if c == -2:
                q = q * 1j
            elif c == -1:
                q = q / 1j
            else:
                for _ in range(c):
                    if p + q in obstacles:
                        break
                    p += q
                    ans = max(ans, round(abs(p) ** 2))
        return ans
```

# 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

```python3
arr = [4, 5, 6, 7, 0, 1, 2]
arr2 = [6, 7, 8, 1, 2, 3, 4, 5]


def find_point(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[left] > arr[mid] and arr[right] > arr[mid]:
            return mid

        if arr[mid] > arr[right]:
            left = mid

        if arr[mid] < arr[left]:
            right = mid

print(arr, " => ", find_point(arr))
print(arr2, " => ", find_point(arr2))

"""
[4, 5, 6, 7, 0, 1, 2]  =>  4
[6, 7, 8, 1, 2, 3, 4, 5]  =>  3
"""

```

# 岛屿数量

```python3
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
```


# 单词接龙

BFS可以用来解决“最短”问题

```python3
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        visited = {beginWord}

        queue = deque()
        queue.append(beginWord)

        word_len = len(beginWord)
        step = 1

        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()
                word_list = list(word)

                for j in range(word_len):
                    origin_char = word_list[j]
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)

                    word_list[j] = origin_char
            step += 1
        return 0
```

# 搜索旋转排序数组

```python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        if nums[left] == target:
            return left
        else:
            return -1
```