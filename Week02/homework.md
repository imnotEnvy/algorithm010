本周作业
简单：
- [ ]写一个关于 HashMap 的小总结。
说明：对于不熟悉 Java 语言的同学，此项作业可选做。
- [x] 有效的字母异位词（亚马逊、Facebook、谷歌在半年内面试中考过）
- [x] 两数之和（近半年内，亚马逊考查此题达到 216 次、字节跳动 147 次、谷歌 104 次，Facebook、苹果、微软、腾讯也在近半年内面试常考）
- [x] N 叉树的前序遍历（亚马逊在半年内面试中考过）
- [ ] HeapSort ：自学 https://www.geeksforgeeks.org/heap-sort/
中等：
- [ ] 字母异位词分组（亚马逊在半年内面试中常考）
- [x] 二叉树的中序遍历（亚马逊、字节跳动、微软在半年内面试中考过）
- [x] 二叉树的前序遍历（字节跳动、谷歌、腾讯在半年内面试中考过）
- [x] N 叉树的层序遍历（亚马逊在半年内面试中考过）
- [x] 丑数（字节跳动在半年内面试中考过）
- [x] 前 K 个高频元素（亚马逊在半年内面试中常考）

# 有效的字母异位词
[LeetCode.242](https://leetcode-cn.com/problems/valid-anagram/submissions/)

**审题**：

**关键思路**：
1. 用哈希表计算字母出现的次数
2. 在s中出现一次+1, 在t中出现一次-1

```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False
        else:
            m = defaultdict(int)
            for i in range(len(s)):
                m[s[i]] += 1
                m[t[i]] -= 1

            for k, v in m.items():
                if v != 0:
                    return False
        return True
```

# 两数之和

```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        # brute-force
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        # hashmap
        map_ = {nums[0]: 0}

        for i in range(1, len(nums)):
            left = target - nums[i]
            if left in map_:
                return map_.get(left), i

            map_[nums[i]] = i
        return []
```

# N 叉树的前序遍历

先访问当前节点，然后依次遍历子节点

```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        result = []
        def traverse(root, result) -> None:
            if root:
                result.append(root.val)
                for c in root.children:
                    traverse(c, result)
        traverse(root, result)
        return result
```

# 二叉树的中序遍历

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traverse(root: TreeNode) -> None:
            if root:
                traverse(root.left)
                result.append(root.val)
                traverse(root.right)
        traverse(root)
        return result
```

# 二叉树的前序遍历

```python3

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def traverse(root: TreeNode) -> None:
            if root:
                result.append(root.val)
                traverse(root.left)
                traverse(root.right)

        traverse(root)
        return result
```

# N 叉树的层序遍历

**关键思路**：
1.使用前序遍历解决层序遍历问题

```python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []

        def traverse(root, depth):
            if root is None: return
            if depth >= len(result):
                result.append([])
            result[depth].append(root.val)
            for c in root.children:
                traverse(c, depth + 1)

        traverse(root, 0)
        return result
```

# 丑数

```python3
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0: return False

        while num != 1:
            if num % 2 == 0: num /= 2
            elif num % 3 == 0: num /= 3
            elif num % 5 == 0: num /= 5
            else: return False

        return True
```

# 前K个高频元素

1. 使用Hashmap和堆实现获取前K个高频元素

```python3
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
```