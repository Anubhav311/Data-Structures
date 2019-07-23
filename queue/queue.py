class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    self.size = len(self.storage)
  
  def dequeue(self):
    if len(self.storage) > 0:
      self.size = len(self.storage) - 1
      return self.storage.pop(0)

  def len(self):
    # self.size = len(self.storage)
    return self.size
