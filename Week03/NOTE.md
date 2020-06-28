# 学习笔记

# 递归和其问题
#a-算法训练营

# 递归
## 判断一个问题是否是“递归问题”
寻找问题中的是否存在子问题，是否存在**最近重复子问题**。
递归问题的解 基于递归子问题的解构建的。

一般思路：
- 自底向上的递归
	- 解法直观，容易理解，但是思考问题可能并不直观
	- 关键：**基于上一种情况的答案（或者前面所有情况）**得出后一种情况的解
- 自上而下的递归
	- 思考问题直观
	- 解法（代码）可能不容易理解
	- **试着对N变量（可能是一个或者一组变量）进行子问题分析和拆分，并注意子问题是否有重叠**
- 数据分割的递归
	- 对数据集拆分成两半（归并排序，快速排序）

## 递归的复杂度分析
### 空间复杂度
递归调用会占用 系统调用栈 的空间，最少占用O(n)

### 时间复杂度
可以使用“递归树”来辅助分析时间复杂度。

运行每个节点是O(1)，一个深度为n的递归树，节点最大有 2^n - 1,  所以复杂度 O(2^n)

## 递归与迭代
**所有的递归都可以用迭代实现**，但是可能会使代码的相当复杂。

## 递归代码模版

```python3

def recur():

    # terminates when

    # current level logic

    # drill down

    # 处理递归从下层返回回来时的逻辑
    # 1. 合并子问题
    # 2. 清理因为递归函数调用对环境带来的side-effects
    # 3. 无逻辑

# Python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
	   process_result
	   return
    # process logic in current level
    process(level, data...)
    # drill down
    self.recursion(level + 1, p1, ...)
    # reverse the current level status if needed
```

# 分治

## 代码模版

```python3
# Python
def divide_conquer(problem, param1, param2, ...):
  # recursion terminator
  if problem is None:
	print_result
	return
  # prepare data
  data = prepare_data(problem)
  subproblems = split_problem(problem, data)
  # conquer subproblems
  subresult1 = self.divide_conquer(subproblems[0], p1, ...)
  subresult2 = self.divide_conquer(subproblems[1], p1, ...)
  subresult3 = self.divide_conquer(subproblems[2], p1, ...)
  …
  # process and generate the final result
  result = process_result(subresult1, subresult2, subresult3, …)

  # revert the current level states
```

# 回溯

回溯法可以说是一种“暴力解法”的升级版，回溯法解决的问题可以用树状结构来表示

解决一个回溯问题，实际上就是一个决策树的遍历过程，如果在叶子节点的状态满足题目的约束条件，则得到了一个有效的 解，如果遍历完整个决策树后仍然达不到约束条件，则问题无解

回溯法的三个关键概念
1、路径：也就是已经做出的选择。
2、选择列表：也就是你当前可以做的选择。
3、结束条件：也就是到达决策树底层，无法再做选择的条件。

## 代码模版

```
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

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
        return resul
```


多叉树的遍历

```python3

def n_tree_traverse(root):
    if root:
        for c in root.children:
            # preorder -> 作出选择
            n_tree_traverse(c)
            # postorder -> 撤销选择
```