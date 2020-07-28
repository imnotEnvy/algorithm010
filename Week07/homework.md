本周作业
简单
- [ ] 爬楼梯（阿里巴巴、腾讯、字节跳动在半年内面试常考）
中等
- [x] 实现 Trie (前缀树) （亚马逊、微软、谷歌在半年内面试中考过）
- [x]朋友圈（亚马逊、Facebook、字节跳动在半年内面试中考过）
- [x]岛屿数量（近半年内，亚马逊在面试中考查此题达到 361 次）
- [ ]被围绕的区域（亚马逊、eBay、谷歌在半年内面试中考过）
- [ ]有效的数独（亚马逊、苹果、微软在半年内面试中考过）
- [ ]括号生成（亚马逊、Facebook、字节跳动在半年内面试中考过）
- [ ]单词接龙（亚马逊、Facebook、谷歌在半年内面试中考过）
- [ ]最小基因变化（谷歌、Twitter、腾讯在半年内面试中考过）
困难
- [ ]单词搜索 II （亚马逊、微软、苹果在半年内面试中考过）
- [ ]N 皇后（亚马逊、苹果、字节跳动在半年内面试中考过）
- [ ]解数独（亚马逊、华为、微软在半年内面试中考过）


# 实现Trie

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self._end_of_word = '#'


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        _node = self.root
        for char in word:
            _node = _node.setdefault(char, {})
        _node[self._end_of_word] = self._end_of_word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        _node = self.root
        for char in word:
            _node = _node.get(char, None)
            if _node is None:
                return False
        return self._end_of_word in _node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        _node = self.root
        for char in prefix:
            _node = _node.get(char, None)
            if _node is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```


# 朋友圈

```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        if not M: return 0

        n = len(M)

        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.union(p, i, j)
        return len(set([self.parent(p, i) for i in range(n)]))

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i: # 路径压缩 ?
            x = i; i = p[i]; p[x] = root
        return root
```

# 岛屿数量

错误记录：(调试了才发现错误)
二维数组坐标 对于 单个数组的下标
(i, j) -> i * n_col + j
X: (i, j) -> i * n_row + j

```python3
#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        m = len(grid)
        n = len(grid[0])

        disju_set = DisjointUnionSet(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        _i, _j = i + di, j + dj
                        if 0 <= _i < m and 0 <= _j < n and grid[_i][_j] == '1':
                            disju_set.union(n * _i + _j, n * i + j)

        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands.add(disju_set.find(n * i + j))

        return len(islands)

# @lc code=end

class DisjointUnionSet(object):

    def __init__(self, n) -> None:
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
        self.n = n

    def find(self, x):
        try:
            if self.parent[x] != x:
                return self.find(self.parent[x])
            return x
        except:
            print(x)
            raise Exception

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1
```