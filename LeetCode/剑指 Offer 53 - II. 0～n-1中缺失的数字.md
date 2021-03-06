# **剑指 Offer 53 - II. 0～n-1中缺失的数字**

### 题目描述

难度简单278收藏分享切换为英文接收动态反馈

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

**示例 1:**

```
输入: [0,1,3]
输出: 2

```

**示例 2:**

```
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
```

**限制：**

`1 <= 数组长度 <= 10000`

### 题解

```jsx
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
  let left = 0, right = nums.length - 1

  if (right === 0) return nums[right] === 0
    ? 1
    : 0

  if (nums[left] !== 0) return 0

  while(left < right) {
    const mid = Math.floor((left + right) / 2)

    // 往左侧寻找
    for (let i = left; i <= mid; i++) {
      if (nums[i] + 1 !== nums[i + 1]) {
        return nums[i] + 1 // 缺失的数字
      }
    }

    left = mid + 1
  }

  return nums[right] - 1 === nums[right - 1]
    ? nums[right] + 1
    : nums[right] - 1
};
```