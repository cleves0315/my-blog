# **剑指 Offer 24. 反转链表**

### 题目描述

难度简单443收藏分享切换为英文接收动态反馈

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

**示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

**限制：**

`0 <= 节点个数 <= 5000`

### 题解 · 一

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  let list = []

  if (!head) return head

  while(head) {
    list.unshift(head)
    head = head.next
  }

  for (let i = 0; i < list.length; i++) {
    if (i + 1 !== list.length) {
      list[i].next = list[i+1]
    } else {
      list[i].next = null
    }
  }

  return list[0]
};
```

### 题解 · 二

花了一晚上捋清楚了大体思路，这里记录下

### **解题思路**

![https://pic.leetcode-cn.com/1654534324-hbiIJz-www.tldraw.com_.png](https://pic.leetcode-cn.com/1654534324-hbiIJz-www.tldraw.com_.png)

- 迭代这个链表
- 记录每次的上个值
- 然后把当前的下个节点，指向上个存储的值
- 达成反转（这就是核心思路）

### **代码**

```jsx
let pre = null

while(head) {

const curr = head

curr.next = pre // 每次指向上个存储的值

pre = curr // 保存下来，供下个节点指向

head = head.next

}
```

但是上面的代码有问题，因为引用数据类型存储在堆空间，这样做会影响到原始链表 (head)

### **重点！！！**

![https://pic.leetcode-cn.com/1654534958-tInQfw-www.tldraw.com_%20(1).png](https://pic.leetcode-cn.com/1654534958-tInQfw-www.tldraw.com_%20(1).png)

- 先把下个节点提取出来
- 斩断它们的姻缘（连接）！！！这样更改 curr 就不会影响 next
- 按上面的核心思路，把 curr 的 next 指向 pre
- 然后借用已经斩断的 next，进入下个节点（重复上面的操作）
- 从而解决了引用数据类型影响的问题

### **代码**

```jsx
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  let pre = null, curr = head

  while(curr) {
    const next = curr.next
    curr.next = pre
    pre = curr
    curr = next
  }

  return pre
};
```