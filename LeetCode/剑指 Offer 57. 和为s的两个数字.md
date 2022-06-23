# **剑指 Offer 57. 和为s的两个数字**

### 题目描述

难度简单191收藏分享切换为英文接收动态反馈

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

```

**示例 2：**

```
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

```

**限制：**

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

### 题解一

```jsx
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  const map = new Map()

  for (let i = 0; i < nums.length; i++) {
    if (map.has(nums[i])) {
      return [target - nums[i], nums[i]]
    } else {
      map.set(target - nums[i])
    }
  }
};

作者：cleves
链接：https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/js-liang-chong-ti-jie-by-cleves-0lda/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

### 题解二
```jsx
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let i = 0, j = nums.length - 1

  while (true) {
    if (nums[i] + nums[j] === target) {
      return [nums[i], nums[j]]
    }
    if(nums[i] + nums[j] < target) {
      i++
    } else {
      j--
    }
  }  
};

作者：cleves
链接：https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/js-liang-chong-ti-jie-by-cleves-0lda/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```