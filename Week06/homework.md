# 习题

- [x][最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)
- [x][解码方法](https://leetcode-cn.com/problems/decode-ways)
- [x][最大正方形](https://leetcode-cn.com/problems/maximal-square/)
- [ ][任务调度器](https://leetcode-cn.com/problems/task-scheduler/)
- [x][回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)
- [x][最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)
- [ ][编辑距离](https://leetcode-cn.com/problems/edit-distance/)
- [ ][矩形区域不超过 K 的最大数值和](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/)
- [ ][青蛙过河](https://leetcode-cn.com/problems/frog-jump/)
- [ ][分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum)
- [ ][学生出勤记录 II ](https://leetcode-cn.com/problems/student-attendance-record-ii/)
- [ ][最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)
- [x][戳气球](https://leetcode-cn.com/problems/burst-balloons/)



# 最小路径和

```python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[None for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = dp[0][0]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]
```


# 解码方法

```python3

# 递归分治法
memo = {}
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0: return 1
        cnt = 0
        rv = memo.get(s, None)
        if rv:
            return rv
        if s[0] != '0':
            cnt += self.numDecodings(s[1:])
        if 10 <= int(s[0:2]) <= 26:
            cnt += self.numDecodings(s[2:])
        memo[s] = cnt
        return cnt

# 动态规划
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(1, len(s)):
            dp[i + 1] += dp[i] * (s[i] != '0') + dp[i - 1] * ('10' <= s[i-1:i+1] <= '26')

        return dp[-1]
```


# 最大正方形

```python3
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        max_side = 0
        m, n = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side
```

# 回文子串

```
base:
dp: dp[i][j], s[i:j+1] 是否为回文串，
状态转移方程: dp[i][j] = d[i+1][j-1] + 1, (s[i] == s[j])
                       = 1, len(s[i:j]) < 2
```

```python3
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i, -1, -1):
                if s[j] == s[i] and ((i - j < 2) or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    ans += 1
        return ans
```


# 最长有效括号

```python3
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        ans, stack = 0, [-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans


```

# 戳气球

```python3
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        nums = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = nums[i] * nums[k] * nums[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        return dp[0][-1]
```