'''
Leetcode : 237
Problem Statement : https://leetcode.com/problems/delete-node-in-a-linked-list/description/
Approach:

Since we do not have access to the head of the list, we cannot traverse the list from the beginning. 
Instead, we can copy the data from the next node into the current node, and then delete the next node.

Here is a step-by-step breakdown:

	1.	Copy the value from the next node to the current node.
	2.	Link the current node to the node after the next node.
	3.	The next node is effectively removed from the list, and the value in the current node is replaced with the next node’s value.

Code Implementation:
'''
# Defination of a singly linked list
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def delete_node(node):
    # copy the value of next node to the current node
    node.value = node.next.value
    # skip the next node
    node.next = node.next.next

#EXAMPLE USAGE
# 1 -> 5 -> 3 -> 4 -> 9 WHERE N = 5
# COPY NODE.NEXT.VALUE TO NODE.VALUE (node.value = node.next.value)
# 1 -> 3 ->   -> 4 -> 9 
# SKIP THE NEXT NODE
# NODE.NEXT = NODE.NEXT.NEXT
# 1 -> 3 -> 4 -> 9 
    