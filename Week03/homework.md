# 本周作业

中等：
- [x] 二叉树的最近公共祖先（Facebook 在半年内面试常考）
- [] 从前序与中序遍历序列构造二叉树（字节跳动、亚马逊、微软在半年内面试中考过）
- [x] 组合（微软、亚马逊、谷歌在半年内面试中考过）
- [x] 全排列（字节跳动在半年内面试常考）
- [x] 全排列 II （亚马逊、字节跳动、Facebook 在半年内面试中考过）

# 二叉树的最近公共祖先

关键思路：
1. 后序遍历二叉树，判断节点是否在二叉树的左右子树中
2. 定义子问题：左右子树分别包括p, q, 或者节点本身等于p或者q

```python3
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        result = None
        def dfs(root, p, q):
            nonlocal result
            if root is None: return False

            lson = dfs(root.left, p, q)
            rson = dfs(root.right, p, q)

            if (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
                result = root
            return lson or rson or (root.val == p.val or root.val == q.val);

        dfs(root, p, q)
        return result
```

# 从前序与中序遍历序列构造二叉树（字节跳动、亚马逊、微软在半年内面试中考过）

关键思路：
1。

```python3

```


# 组合

关键思路：
1. 回溯法

```python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(number, comb):
            if len(comb) == k:
                result.append(comb[:])

            for i in range(number, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return result

```

# 全排列

关键思路：
1. 回溯法

```python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(nums: List[int], path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])  # can't append reference here
                return

            for x in nums:
                if x in path:
                    continue
                path.append(x)
                backtrack(nums, path)
                path.pop()

        backtrack(nums, [])
        return result
```

# 全排列2


关键思路：
1. 回溯法
2. 使用数组配合下标用来当作高效的查询结构，判断一个数是否以及被使用干活

```python3
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        result = []
        used = [False for _ in range(len(nums))]

        def backtrack(nums, path, size):
            if len(path) == size:
                result.append(path[:])
                return

            for i, x in enumerate(nums):
                if not used[i]:


                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(x)
                    backtrack(nums, path, size)
                    used[i] = False
                    path.pop()


        backtrack(nums, [], len(nums))
        return result
```