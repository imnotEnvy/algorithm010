# 作业

简单

- [x] 位 1 的个数（Facebook、苹果在半年内面试中考过）
- [x] 2 的幂（谷歌、亚马逊、苹果在半年内面试中考过）
- [x] 颠倒二进制位（苹果在半年内面试中考过）
- [ ] 用自己熟悉的编程语言，手写各种初级排序代码，提交到学习总结中。
- [x] 数组的相对排序（谷歌在半年内面试中考过）
- [ ] 有效的字母异位词（Facebook、亚马逊、谷歌在半年内面试中考过）

中等

- [x] LRU 缓存机制（亚马逊、字节跳动、Facebook、微软在半年内面试中常考）
- [ ] 力扣排行榜（Bloomberg 在半年内面试中考过）
- [ ] 合并区间（Facebook、字节跳动、亚马逊在半年内面试中常考）

困难
- [ ] N 皇后（字节跳动、亚马逊、百度在半年内面试中考过）
- [ ] N 皇后 II （亚马逊在半年内面试中考过）
- [ ] 翻转对（字节跳动在半年内面试中考过）


# 位1的个数

```python3
class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0
        while n != 0:
            n &= n - 1
            cnt += 1
        return cnt
```

# 2的幂

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & (n - 1) == 0
```

# 颠倒二进制位

```python3
class Solution:
    def reverseBits(self, n: int) -> int:
        ans, power = 0, 31

        while n:
            ans += (n & 1) << power
            n = n >> 1
            power -= 1

        return ans
```


# LRU缓存机制

```python3
class LRUCache(object):

	def __init__(self, capacity):
		self.dic = collections.OrderedDict()
		self.remain = capacity

	def get(self, key):
		if key not in self.dic:
			return -1
		v = self.dic.pop(key)
		self.dic[key] = v
		return v

	def put(self, key, value):
		if key in self.dic:
			self.dic.pop(key)
		else:
			if self.remain > 0:
				self.remain -= 1
			else:
				self.dic.popitem(last=False)
		self.dic[key] = value
```

# 数组的相对排序

```python3
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))
```