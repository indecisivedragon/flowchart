'''
Created on Jan 21, 2017

@author: Lili
'''

from src.graphics.Node import Node

# links two different elements in a chart using an arrow
# although right now it is just a line
class Edge(object):
  def __init__(self, source_node, destination_node):
    # each edge has a source and a destination
    # this is a directed graph I guess?
    self.source = source_node
    self.destination = destination_node
    
    self.coordinates_start = (0, 0)
    self.coordinates_end = (0, 0)
  
  def compute_coordinates(self):
    # start at end of source node (right side)
    self.coordinates_start = self.source.get_right_coordinates()
    
    # end at beginning of destination node (left side)
    self.coordinates_end = self.destination.get_left_coordinates()
  
  # returns a string of start and end
  def to_string(self):
    if (self.source.name is not None):
      source_name = self.source.name
    else:
      source_name = "unknown"
      
    if (self.destination.name is not None):
      dest_name = self.destination.name
    else:
      dest_name = "unknown"
    
    return "start: " + source_name + ", end: " + dest_name


if __name__ == "__main__":
  print("this is the edge testing")
  node = Node("start")
  node.set_coordinates(100, 30)
  node.print()
  
  node2 = Node("end")
  node2.set_coordinates(200, 50)
  node2.print()
  
  edge = Edge(node, node2)
  edge.compute_coordinates()
  print(edge.coordinates_start, "to", edge.coordinates_end)
  