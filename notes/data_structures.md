# Data Structures Reference

## Arrays
- Fixed-size sequential collection of same-type elements
- Access: O(1), Search: O(n), Insert/Delete: O(n)

## Linked List
- Linear collection where each element points to the next
- Access: O(n), Insert/Delete at head: O(1)

## Stack (LIFO)
- Last In, First Out
- Push/Pop: O(1)
- Use cases: undo operations, call stack, expression parsing

## Queue (FIFO)
- First In, First Out
- Enqueue/Dequeue: O(1)
- Use cases: BFS, task scheduling, print queue

## Hash Table
- Key-value storage with O(1) average access
- Collisions handled via chaining or open addressing

## Binary Tree
- Each node has at most 2 children
- BST: Left < Root < Right
- Traversals: Inorder, Preorder, Postorder

## Heap
- Complete binary tree where parent >= children (max-heap)
- Insert/Delete: O(log n), Find max/min: O(1)

## Graph
- Nodes (vertices) connected by edges
- Directed/Undirected, Weighted/Unweighted
