# **剑指 Offer 32 - I. 从上到下打印二叉树**

### 题目描述

难度中等213收藏分享切换为英文接收动态反馈

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7

```

返回：

```
[3,9,20,15,7]

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
 * @return {number[]}
 */
var levelOrder = function(root) {
  let stack = [root]
  const ans = []

  if(!root) {
    return []
  }

  while(stack.length) {
    const nodes = []
    while(stack.length) {
      const node = stack.shift()
      ans.push(node.val)

      if(node.left) {
        nodes.push(node.left)
      }
      if(node.right) {
        nodes.push(node.right)
      }
    }
    stack = [...nodes]
  }

  return ans
};
```