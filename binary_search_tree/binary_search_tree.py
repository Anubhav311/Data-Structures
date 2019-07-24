class BinarySearchTreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTreeNode(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTreeNode(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False
    elif target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    temp = self
    
    while temp.right is not None:
      temp = temp.right
    return temp.value

  def for_each(self, cb):
    pass