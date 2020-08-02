学习笔记

# 位运算

基本运算
```
x >> 1 右移
x << 1 左移

|, 或
&, 与
~, 取反
^, 异或

```

## 奇偶性分析

```python
x & 1 == 1  # 奇数
x & 1 == 0  # 偶数
```

## 乘以2

设想 100 右移一位为 10，原数字为之前的1/10。
对于二进制，右移一位则缩小 1/2。

`x / 2 == x >> 1`

## 常见

- `x & (x - 1)` 清除最后一个1
- `x & 1` 获取最右边一位
- `(x >> n) & 1`, 获取最右边向左偏移n位的一位的值
    ```
    In [30]: (1101 >> 1) & 1
    Out[30]: 0

    In [31]: (1101 >> 0) & 1
    Out[31]: 1

    In [32]: (1101 >> 2) & 1
    Out[32]: 1
    ```
- `x & -x` 获取最低位的1
- `x & ~x` =0


# Bloom Filter

使用场景：判断一个元素是否存在于一个集合中，常用于去重场景。

ps: 具体要确认一个元素是否存在，还是需要在业务数据检索

优点：
- 优于一般算法的空间和时间复杂度

缺点：
- 有一定的误判率
- 删除困难

```python
# Python
from bitarray import bitarray
import mmh3
class BloomFilter:
	def __init__(self, size, hash_num):
		self.size = size
		self.hash_num = hash_num
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)
	def add(self, s):
		for seed in range(self.hash_num):
			result = mmh3.hash(s, seed) % self.size
			self.bit_array[result] = 1
	def lookup(self, s):
		for seed in range(self.hash_num):
			result = mmh3.hash(s, seed) % self.size
			if self.bit_array[result] == 0:
				return "Nope"
		return "Probably"
bf = BloomFilter(500000, 7)
bf.add("dantezhao")
print (bf.lookup("dantezhao"))
print (bf.lookup("yyj"))
```


# LRU Cache

最近最少使用缓存

一个元素被使用后，刷新元素的缓存位置，如果空间不够，淘汰的元素就是最近最少被使用的元素。

```python
# Python
class LRUCache(object):

	def __init__(self, capacity):
		self.dic = collections.OrderedDict()
		self.remain = capacity

	def get(self, key):
		if key not in self.dic:
			return -1
		v = self.dic.pop(key)
		self.dic[key] = v   # key as the newest one
		return v

	def put(self, key, value):
		if key in self.dic:
			self.dic.pop(key)
		else:
			if self.remain > 0:
				self.remain -= 1
			else:   # self.dic is full
				self.dic.popitem(last=False)
		self.dic[key] = value
```

常见实现方式：双向链表 + 哈希表


# 排序算法

排序算法的分类
- 比较排序
    通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn),因此也称为非线性时间比较类排序
    - 交换排序
        - 冒泡排序
        - ！快速排序
    - 插入排序
        - 简单插入排序
        - shell排序
    - 选择排序
        - 简单选择排序
        - ！堆排序
    - 归并排序
        - ！二路归并排序
        - 多路归并排序
- 非比较排序
    通过比较来决定元素间的相对次序, 由于其时间复杂度可以达到线性时间，因此也称为线性时间非比较类排序
    - 计数排序
    - 桶排序
    - 基数排序


代码


```python

# 冒泡排序
def bubble_sort(arr):
    size = len(arr)

    if size <= 1:
        return arr

    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
    return arr

# 选择排序
def select_sort(arr):
    size = len(arr)

    for i in range(0, size - 1):
        min_idx = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr

# 比较计数排序
def compare_and_count_sort(arr):
    size = len(arr)
    count = [0] * size
    res = [None] * size
    for i in range(size-1):
        for j in range(i+1, size):
            if arr[i] < arr[j]:
                count[j] = count[j] + 1
            else:
                count[i] = count[i] + 1
    for i in range(size):
        res[count[i]] = arr[i]
    return res

# 快速排序
def quick_sort(items):
    size = len(items)

    if size <= 1:
        return items

    pivot_idx = random.randint(0, size - 1)
    pivot = items[pivot_idx]
    lt_part = [item for item in items if item < pivot]
    gte_part = [item for idx, item in enumerate(
        items) if item >= pivot and idx != pivot_idx]
    return quick_sort(lt_part) + [pivot] + quick_sort(gte_part)


# 归并排序
def merge_sort(items, left, right):

    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(items, left, mid)
        merge_sort(items, mid, right)
        merge(items, left, mid, right)
    return items

def merge(items, left, mid, right):
    left_part = items[left:mid]
    right_part = items[mid:right]

    left_part.append(float('inf'))
    right_part.append(float('inf'))

    i, j = 0, 0
    for k in range(left, right):
        if left_part[i] <= right_part[j]:
            items[k] = left_part[i]
            i += 1
        else:
            items[k] = right_part[j]
            j += 1


```
