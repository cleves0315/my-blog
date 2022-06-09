# **剑指 Offer 53 - I. 在排序数组中查找数字 I**

### 题目描述

难度简单322收藏分享切换为英文接收动态反馈

统计一个数字在排序数组中出现的次数。

**示例 1:**

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```

**示例 2:**

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```

**提示：**

- `0 <= nums.length <= 105`
- `109 <= nums[i] <= 109`
- `nums` 是一个非递减数组
- `109 <= target <= 109`

### 题解

- 根据题目得到 nums 是排序数组
- 取数组中间值 mid
- nums[mid] > target 目标值就在 mid 左侧，反之在右侧
- 直到找到目标值，再以找到的位置往两边查找相同的数量即可

```jsx
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
  let left = 0, right = nums.length - 1, num = 0
  
  while(left <= right) {
    const mid = Math.floor((left + right) / 2)

    if (target === nums[mid]) {
      let n = mid
      while(nums[n++] === target) {
        num++
      }
      n = mid - 1
      while(nums[n--] === target) {
        num++
      }
      break
    }

    if (target > nums[mid]) {
      left = mid + 1
    } else {
      right = mid - 1
    }
  }

  return num
};
```