'''
Created on Jan 21, 2017

@author: Lili
'''

class Node(object):
  
  # a class to store the elements that we must draw
  def __init__(self, name):
    self.name = name
    
    # the attached nodes of all edges incident into and out of this particular node
    self.indegree_nodes = []
    self.outdegree_nodes = []
    
    # position on the chart (upper left edge to be consistent with pygame)
    # the axes are always flipped and it's very confusing!
    self.coordinates = (0, 0)
    
    # default text size
    self.height = 15
    self.width = 100
    
  def set_coordinates(self, x, y):
    self.coordinates = (x, y)
  
  def set_text_size(self, font_size):
    self.height = font_size
    self.width = len(self.name) * font_size * (0.7)
    
  def get_left_coordinates(self):
    x = self.coordinates[0] - 10
    y = self.coordinates[1] + self.height*(0.5)
    return (x, y)
  
  def get_right_coordinates(self):
    x = self.coordinates[0] + self.width
    y = self.coordinates[1] + self.height*(0.5)
    return (x, y)
  
  def print(self):
    output = self.name + " at "
    print(output, self.coordinates)
  
if __name__ == "__main__":
  print("hello")
  node = Node("test")
  node.set_coordinates(100, 30)
  print(node.coordinates)
  print(node.get_left_coordinates())