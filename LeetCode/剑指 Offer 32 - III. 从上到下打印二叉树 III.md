# **剑指 Offer 32 - III. 从上到下打印二叉树 III**

### 题目描述

难度中等235收藏分享切换为英文接收动态反馈

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7

```

返回其层次遍历结果：

```
[
  [3],
  [20,9],
  [15,7]
]

```

**提示：**

1. `节点总数 <= 1000`

### 题解

```jsx
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
  let stack = [root],
    ans = [],
    b = true // false: 左到右，true: 右到左

  if(!root) {
    return []
  }

  while(stack.length) {
    const vals = [], list = []

    while(stack.length) {
      let node = stack.shift()
      vals.push(node.val)

      if(!b) {
        if(node.right) {
          list.unshift(node.right)
        }
        if(node.left) {
          list.unshift(node.left)
        }
      } else {
        if(node.left) {
          list.unshift(node.left)
        }
        if(node.right) {
          list.unshift(node.right)
        }
      }
    }

    b = !b // 切换下次方向
    stack = [...list]
    ans.push([...vals])
  }

  return ans
};
```