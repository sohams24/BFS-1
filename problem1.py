'''
Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)

Time Complexity: O(n)
Space Complexity: 
- O(n) using BFS
- O(h) using DFS

'''
# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

#------------------------------Breadth First Search---------------------------------
from collections import deque

class Solution:
  def levelOrder(self, root):
    if not root:
      return []
    bfsQueue = deque([root])
    levelOrder = []
    while len(bfsQueue) > 0:
      size = len(bfsQueue)
      level = []
      for i in range(size):
        node = bfsQueue.popleft()
        level.append(node.val)
        if node.left:
          bfsQueue.append(node.left)
        if node.right:
          bfsQueue.append(node.right)
      levelOrder.append(level)
    return levelOrder

#------------------------------Depth First Search---------------------------------
class Solution:
  def levelOrder(self, root):
    if not root:
      return []
    levelOrder = []
    self.dfs(root, 0, levelOrder)
    return levelOrder

  def dfs(self, root, currentLevel, levelOrder):
    if len(levelOrder) > currentLevel:
      levelOrder[currentLevel].append(root.val)
    else:
      levelOrder.append([root.val])

    if root.left:
      self.dfs(root.left, currentLevel + 1, levelOrder)
    if root.right:
      self.dfs(root.right, currentLevel + 1, levelOrder)
