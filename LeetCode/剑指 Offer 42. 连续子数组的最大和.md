# **剑指 Offer 42. 连续子数组的最大和**

### 题目描述

难度简单545收藏分享切换为英文接收动态反馈

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

**示例1:**

```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

**提示：**

- `1 <= arr.length <= 10^5`
- `100 <= arr[i] <= 100`

### 题解

```jsx
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  let max = nums[0], sum = nums[0]

  for(let i = 1; i < nums.length; i++) {
    const sum1 = sum + nums[i]

    if (nums[i] > sum1) {
      sum = nums[i]
    } else {
      sum = sum1
    }
    max = Math.max(sum, max)
  }

  return max
};
```