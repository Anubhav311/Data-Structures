class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    topValue = self.storage[0]
    self.storage[0] = self.storage[-1]

    del(self.storage[-1])

    self._sift_down(0)
    return topValue

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent

      else:
        break

  def _sift_down(self, index):
    largerChildrenIndex = (index * 2) + 1

    if ((index * 2) + 2) < len(self.storage):
      if self.storage[largerChildrenIndex] < self.storage[(index * 2) + 2]:
        largerChildrenIndex = (index * 2) + 2
      
      if self.storage[index] < self.storage[largerChildrenIndex]:
        self.storage[largerChildrenIndex], self.storage[index] = self.storage[index], self.storage[largerChildrenIndex]
        self._sift_down(largerChildrenIndex)
        
    elif ((index * 2) + 1) < len(self.storage):
      if self.storage[index] < self.storage[largerChildrenIndex]:
        self.storage[largerChildrenIndex], self.storage[index] = self.storage[index], self.storage[largerChildrenIndex]
        self._sift_down(largerChildrenIndex)

