class Height(object):
  def __init__(self):
    self.height = 0

class NodeBT(object):
  def __init__(self, value=None, level=1):
    self.value = value
    self.level = level
    self.left  = None
    self.right = None
  
  def __repr__(self):
    return "{}".format(self.value)
