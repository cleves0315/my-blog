# **剑指 Offer 39. 数组中出现次数超过一半的数字**

### 题目描述

难度简单291收藏分享切换为英文接收动态反馈

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

**示例 1:**

```
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
```

**限制：**

`1 <= 数组长度 <= 50000`

### 题解 · 打表

```jsx
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let max = nums[0]
  const map = new Map()

  for(let i = 0; i < nums.length; i++) {
    if(map.has(nums[i])) {
      const cout = map.get(nums[i])
      map.set(nums[i], cout + 1)
      if(cout + 1 > map.get(max)) {
        max = nums[i]
      }
    } else {
      map.set(nums[i], 1)
    }
  }

  return max
};
```