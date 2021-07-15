class Node:
    def __init__(self, value, nextNode):
      self.value = value
      self.next = nextNode
    
class LinkedList:
  def __init__(self, headVal):
    self.head = Node(headVal, None)
    self.tail = self.head
  def insert(self, nextVal):
    self.tail.next = Node(nextVal, None)
  def traverse(self):
      curr = self.head
      while (curr.next):
        print(curr.value)
        curr = curr.next
      print(curr.value)
  def removeTail(self):
      curr = self.head
      while (curr.next.next):
        curr = curr.next
      del self.tail
      self.tail = curr
      self.tail.next = None

    
animals = LinkedList("Cat")
animals.insert("Dog")
animals.traverse()
animals.removeTail()
print("\n")
animals.traverse()