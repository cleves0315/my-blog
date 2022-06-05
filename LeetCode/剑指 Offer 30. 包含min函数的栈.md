# **剑指 Offer 30. 包含min函数的栈**

### 题目描述

难度简单349收藏分享切换为英文接收动态反馈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

**示例:**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

```

**提示：**

1. 各函数的调用总次数不超过 20000 次

### 题解

```jsx
/**
 * initialize your data structure here.
 */
var MinStack = function() {
  this.mins = [Number.MAX_SAFE_INTEGER]
  this.arr = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
  this.arr.push(x)
  this.mins.push(Math.min(this.mins[this.mins.length-1], x))
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  this.arr.pop()
  this.mins.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  return this.arr[this.arr.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.min = function() {
  return this.mins[this.mins.length - 1]
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.min()
 */
```