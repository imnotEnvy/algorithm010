# Week1 作业

简单：
- [ ] 用 add first 或 add last 这套新的 API 改写 Deque 的代码
- [ ] 分析 Queue 和 Priority Queue 的源码
- [x] 删除排序数组中的重复项（Facebook、字节跳动、微软在半年内面试中考过）
- [x] 旋转数组（微软、亚马逊、PayPal 在半年内面试中考过）
- [x] 合并两个有序链表（亚马逊、字节跳动在半年内面试常考）
- [x] 合并两个有序数组（Facebook 在半年内面试常考）
- [x] 两数之和（亚马逊、字节跳动、谷歌、Facebook、苹果、微软在半年内面试中高频常考）
- [x] 移动零（Facebook、亚马逊、苹果在半年内面试中考过）
- [x] 加一（谷歌、字节跳动、Facebook 在半年内面试中考过）
中等：
- [x] 设计循环双端队列（Facebook 在 1 年内面试中考过）
困难：
- [ ] 接雨水（亚马逊、字节跳动、高盛集团、Facebook 在半年内面试常考）


# Deque代码修改

# Queue和Priority Queue的源码分析

# 删除排序数组中的重复项

[LeetCode.26](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

**审题**：

1. 有序数组
2. 删除重复元素
3. 返回新数组长度，不用管超出新长度的元素
4. 额外空间复杂度: O(1)

**关键思路**：

双指针法，记录下一个不重复元素需要插入的位置。


```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # special conditions:
        if len(nums) <= 1: return len(nums)

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        return i + 1
```

# 旋转数组

[LeetCode.189](https://leetcode-cn.com/problems/rotate-array/)


**审题**：

1. k > 0

**关键思路**：
1. 翻转整个数组后，翻转前k%n个元素，再翻转后面部分元素
2. 环状替换，思路大概懂了，实现上还是有点问题

```python3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # special conditions or prepare
        k = k % len(nums)
        if k == 0: return

        def reverse(nums):
            i, j = 0, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums

        nums = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])

# more Pythonic solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # special conditions or prepare
        k = k % len(nums)
        if k == 0: return

        # nums = nums[::-1]  # not worked?, nums is new variable in function scope,
                             # outside scope "nums" won't be affected

        nums[:] = nums[::-1]  # this worked
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
```


# 合并两个有序链表

[LeetCode.21](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(val=None)
        prev = head

        while l1 and l2:
            prev.next, prev, l1, l2 = (l1, l1, l1.next, l2) if l1.val <= l2.val else (l2, l2, l1, l2.next)

        prev.next = l1 if l1 else l2
        return head.next
```

# 合并两个有序数组

[LeetCode.88](https://leetcode-cn.com/problems/merge-sorted-array/)

**审题**：
1. 有序数组
2. 将nums2合并到nums1中

**关键思路**：
1. 双指针遍历两个数组，将较小值添加到结果数组，并后移一位较小值对应数组的指针
2. 当一个数组遍历完后，遍历另一个数组，遍历值添加到结果值

```python3
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        i = j = k = 0

        while i < m and j < n:
            smaller, i, j = (nums1[i], i+1, j) if nums1[i] <= nums2[j] else (nums2[j], i, j+1)
            result.append(smaller)
            k = k + 1

        if i < m:
            result.extend(nums1[i:m])
        if j < n:
            result.extend(nums2[j:n])

        nums1[:] = result  # update nums1 :)
```


# 两数之和

[LeetCode.1](https://leetcode-cn.com/problems/two-sum/submissions/)

**审题**：
1. 每种输入只有一种答案
2. 不能重复使用元素

**关键思路**：
1. 暴力两次遍历，寻找和相等的两个下标
2. 用hash存储已经遍历过的数值和下标，计算`target - nums[i]`是否已经在hash表中

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


# 移动零

[LeetCode.283](https://leetcode-cn.com/problems/move-zeroes/)

**审题**：
1. 在原数组上进行操作
2. 保持非0元素的相对顺序（不用管0元素的顺序）

**关键思路**：
1. 双指针法，一个指针遍历数组，另一个指针记录下一个非0元素需要插入的位置

```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, x in enumerate(nums):
            if x != 0:
                nums[i], nums[j], j = nums[j], nums[i], j + 1
```


# 加一

[LeetCode.66](https://leetcode-cn.com/problems/plus-one/)

**审题**：
1. 整数组成的非空数组所表示的非负整数
2. 最高位在数组首位, 并且不会以0开头
3. 每位仅存储一个数字

**关键思路**：


```python3

# 反转数组
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_reversed = digits[::-1]
        flag = 0

        for i, x in enumerate(digits_reversed):
            if i == 0:
                x += 1
            x += flag
            flag, x = divmod(x, 10)
            digits_reversed[i] = x
        if flag > 0:
            digits_reversed.append(flag)

        return digits_reversed[::-1]


# 从后往前遍历
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # traverse from right to left
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits

        digits.insert(0, 1)
        return digits
```


# 设计循环双端队列

[LeetCode.641](https://leetcode-cn.com/problems/design-circular-deque/)

**审题**：
1. 双端队列为空返回-1

**关键思路**：
1. 熟练实现代码，如果出现问题，调试比较不方便
2. 多用一位空间来表示front指向位置

```python3
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._queue = [-1 for _ in range(k + 1)]
        self._front = 0
        self._rear = 0
        self._size = k + 1

    def _move(self, start, offset):
        return (start + offset) % self._size

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self._queue[self._front], self._front = value, self._move(self._front, -1)
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        _position = self._move(self._rear, 1)
        self._queue[_position], self._rear = value, _position
        return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._front = self._move(self._front, 1)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._rear = self._move(self._rear, -1)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._queue[self._move(self._front, 1)]


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._queue[self._rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._front == self._rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._move(self._rear, 1) == self._front



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```