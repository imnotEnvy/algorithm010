# 本周作业

## 简单

字符串中的第一个唯一字符
（亚马逊、微软、Facebook 在半年内面试中考过）
反转字符串 II （亚马逊在半年内面试中考过）
翻转字符串里的单词（微软、字节跳动、苹果在半年内面试中考过）
反转字符串中的单词 III （微软、字节跳动、华为在半年内面试中考过）
仅仅反转字母（字节跳动在半年内面试中考过）
同构字符串（谷歌、亚马逊、微软在半年内面试中考过）
验证回文字符串 Ⅱ（Facebook 在半年内面试中常考）

## 中等

在学习总结中，写出不同路径 2 这道题目的状态转移方程。
最长上升子序列（字节跳动、亚马逊、微软在半年内面试中考过）
解码方法（字节跳动、亚马逊、Facebook 在半年内面试中考过）
字符串转换整数 (atoi) （亚马逊、微软、Facebook 在半年内面试中考过）
找到字符串中所有字母异位词（Facebook 在半年内面试中常考）
最长回文子串（亚马逊、字节跳动、华为在半年内面试中常考）

## 困难

最长有效括号（亚马逊、字节跳动、华为在半年内面试中考过）
赛车（谷歌在半年内面试中考过）
通配符匹配（Facebook、微软、字节跳动在半年内面试中考过）
不同的子序列（MathWorks 在半年内面试中考过）


# 字符串中的第一个唯一字符

[leetcode](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)

```python3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1

        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
```

# 反转字符串 II

[leetcode](https://leetcode-cn.com/problems/reverse-string-ii/)

```python3
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)

        for i in range(0, len(a), 2 * k):
            a[i:i+k] = reversed(a[i:i+k])

        return ''.join(a)
```

# 翻转字符串里的单词

[leetcode](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        s = [c for c in s.strip().split(' ') if c]
        return ' '.join(reversed(s))
```

# 反转字符串中的单词 III

[leetcode](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)

```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        return  ' '.join([''.join(reversed(w)) for w in s.split(' ')])
```

# 验证回文字符串 Ⅱ

[leetcode](https://leetcode-cn.com/problems/valid-palindrome-ii/)

```python3
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True
```