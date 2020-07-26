学习笔记

# 字典树Trie

也称为 单词查找树，前序树

n叉树，每个节点存储一个字符，一个到叶子节点的搜索路径表示一个单词。叶子节点为“空”节点。

实现代码模版
```python
# Python
class Trie(object):
	def __init__(self):
		self.root = {}
		self.end_of_word = "#"

	def insert(self, word):
		node = self.root
		for char in word:
			node = node.setdefault(char, {})
		node[self.end_of_word] = self.end_of_word

	def search(self, word):
		node = self.root
		for char in word:
			if char not in node:
				return False
			node = node[char]
		return self.end_of_word in node

	def startsWith(self, prefix):
		node = self.root
		for char in prefix:
			if char not in node:
				return False
			node = node[char]
		return True
```

# 并查集

用来处理判断元素是否在一个集合中的特结构数据。

代码模版:
```python

def init(p):
	# for i = 0 .. n: p[i] = i;
	p = [i for i in range(n)]

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

# 高级搜索

- 剪枝
- 双向BFS
- 启发式搜索