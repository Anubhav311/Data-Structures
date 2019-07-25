class Heap:
  def __init__(self):
    self.storage = []

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def get_parent_index(self, index):
    return (index - 1) // 2

  def get_left_child_index(self, index):
    return index * 2 + 1

  def get_right_child_index(self, index):
    return index * 2 + 2


  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)


  def delete(self):
    topValue = self.storage[0]
    self.storage[0] = self.storage[-1]

    del(self.storage[-1])

    self._sift_down(0)
    return topValue


  def _bubble_up(self, index):
    while index > 0:
      parent = self.get_parent_index(index)
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent

      else:
        break


  def _sift_down(self, index):
    largerChildrenIndex = self.get_left_child_index(index)

    if self.get_right_child_index(index) < len(self.storage):
      if self.storage[largerChildrenIndex] < self.storage[self.get_right_child_index(index)]:
        largerChildrenIndex = self.get_right_child_index(index)
      
      if self.storage[index] < self.storage[largerChildrenIndex]:
        self.storage[largerChildrenIndex], self.storage[index] = self.storage[index], self.storage[largerChildrenIndex]
        self._sift_down(largerChildrenIndex)
        
    elif self.get_left_child_index(index) < len(self.storage):
      if self.storage[index] < self.storage[largerChildrenIndex]:
        self.storage[largerChildrenIndex], self.storage[index] = self.storage[index], self.storage[largerChildrenIndex]
        self._sift_down(largerChildrenIndex)

