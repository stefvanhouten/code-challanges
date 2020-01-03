class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
    return


""" 
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.
Your objective is to determine the length of the loop.
For example in the png of challange5 the tail's size is 3 and the loop size is 11.
"""

#This node chain has a size of 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


def loop_size(node):
  return
