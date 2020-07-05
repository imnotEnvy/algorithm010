学习笔记

# DFS, BFS

DFS，BFS是一种树和图形式的数据结构的基本搜索方式。

DFS使用栈FILO的特性达到一种深度优先的搜索顺序。
BFS使用队列FIFO的特性来达到一种层次优先的搜索顺序。

BFS可以用来解决“最短”问题

在递归问题、回溯问题、动态规划中往往需要通过DFS， BFS的形式对递归树/状态树进行搜索。

## 代码模版

DFS递归模版
```python3
visited = set()
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited
    	return
	visited.add(node)
	# process current node here.
	...
	for next_node in node.children():
		if next_node not in visited:
			dfs(next_node, visited)
```

DFS用栈模拟递归
```python3
def DFS(self, tree):
	if tree.root is None:
		return []
	visited, stack = [], [tree.root]
	while stack:
		node = stack.pop()
		visited.add(node)
		process (node)
		nodes = generate_related_nodes(node)
		stack.push(nodes)
	# other processing work
	...
```

BFS模版

```python3
# Python
def BFS(graph, start, end):
    visited = set()
	queue = []
	queue.append([start])
	while queue:
		node = queue.pop()
		visited.add(node)
		process(node)
		nodes = generate_related_nodes(node)
		queue.push(nodes)
	# other processing work
	...
```

# 贪心算法

贪心算法的效率往往较高

局部的最优选择不一定得到全局的最优解，使用贪心算法需要论证正确性，即局部最优解能推导出全局最优解。


# 二分搜索

二分搜索条件：
1. 单调性
2. 存在上下边界
3. index O(1) 随机访问

二分搜索模版：

```python3
left, right = 0, len(array) - 1
while left <= right:
	  mid = (left + right) / 2
	  if array[mid] == target:
		    # find the target!!
		    break or return result
	  elif array[mid] < target:
		    left = mid + 1
	  else:
		    right = mid - 1
```

二分搜索的思路除了在有序数组中查询某一个数字外，还有其他应用的地方，但是代码需要调整
如： https://leetcode-cn.com/problems/search-in-rotated-sorted-array