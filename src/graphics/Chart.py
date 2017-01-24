'''
Created on Jan 20, 2017

@author: Lili
'''

from src.Section import Section
from src.graphics.Node import Node
from src.graphics.Edge import Edge

import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Chart:
  # constructor
  def __init__(self, filename):
    self.size = (800, 600)
    self.screen = pygame.display.set_mode(self.size)
    
    # text formatting
    self.font_style = "monospace"
    self.font_size = 15
    self.font = pygame.font.SysFont(self.font_style, self.font_size)
    
    self.source_file = filename
    
    self.column_users = {}
    
    self.column_data = {}
    
    self.column_parties = {}
    
    self.edges = []
    
  # construct all columns and edges
  def init(self):
    self._initial_column_setup()
    self._populate_responses(self.source_file)
    
    self._set_distances()
  
  # using a list of responses, construct the columns
  # at the moment we populate the data column (1)
  # and the parties column (2)
  # also we make edges at the same time
  def _populate_responses(self, filename):    
    with open(filename, 'r') as f:
      # create an list of responses we need to go through
      content = f.readlines()
      for i in range(0, len(content)):
        # go through each response document, populating the columns
        file_path = "Response_Data/" + content[i].strip() + "_responses.txt"
        self._add_current_response_section(file_path)    
   
  # initial setup includes adding user and app nodes 
  def _initial_column_setup(self):
    # add user as sole party for first column
    self.column_users["user"] = Node("user")
    
    # add app as party for third column
    self.column_parties["app"] = Node("app")
  
  # for each section, record nodes
  
  # add a certain section
  def _add_current_response_section(self, filename):
    file = open(filename, "r")
    # we read in a json object and decode it as a section
    content = file.read()
    section = Section.json_decode(content)
    
    # for each subsection, add data and parties
    # only if the data is actually collected
    # subroutines automatically check for duplicates
    for i in section.subsections:
      # takes the Data_Source object and adds to the graph as node
      self._handle_subsection_add(i) 
      
  # add column_data node and check for duplicates
  def _handle_subsection_add(self, data_source):
    # if the data is either directly or indirectly collected
    # we want to add it to the column as a node
    if (data_source.get_direct() or data_source.get_indirect()):
      name = data_source.data_type
      node = Node(name)
      self.column_data[name] = node
      
      # user provides the information
      self.edges.append(Edge(self.column_users["user"], node))
      
      # data then goes to...
      if (data_source.get_direct):
        edge = Edge(node, self.column_parties["app"])
        self.edges.append(edge)
      if (data_source.get_indirect):
        third_party = data_source.get_third_party()
        if (third_party is None):
          third_party = "unknown"
        # if this third party isn't already in the parties column, add it
        if not self._check_repeat(third_party, self.column_parties):
          third_party_node = Node(third_party)
          self.column_parties[third_party_node.name] = third_party_node
        # then add the appropriate edge
        edge = Edge(node, self.column_parties[third_party])
        self.edges.append(edge)  
  def _check_repeat(self, name, column):
    repeat = False
    for i in column:
      if i == name:
        repeat = True
    return repeat
  
  # construct a view from the file of which data is collected from reponse_data
  # returns a white-space separated string of things to display
  # only show things that are actually collected

  # x axis distances
  # relative y axis distances
  def _set_distances(self):
    # handle user node(s?)
    # start at column 50
    self._set_distances_column_height_adjust(self.column_users, 50)

    # handle data nodes
    # start at column 250
    self._set_distances_column_height_adjust(self.column_data, 250)
      
    # handle party nodes
    # start at column 450
    self._set_distances_column_height_adjust(self.column_parties, 450)
  
  def _set_distances_column_height_adjust(self, column, x_axis):
    count = 0
    for i in column:
      node = column[i]
      node.set_text_size(self.font_size)
      node.set_coordinates(x_axis, 50 + count*2*self.font_size)
      count = count + 1

  # draw all the nodes in all the columns
  def draw_nodes(self):
    self._draw_individual_column(self.column_users)
    self._draw_individual_column(self.column_data)
    self._draw_individual_column(self.column_parties)

      
  def _draw_individual_column(self, column):
    for i in column:
      label = self.font.render(column[i].name, 1, (0,0,0))
      self.screen.blit(label, column[i].coordinates)
  
  def draw_edges(self):
    for i in self.edges:
      i.compute_coordinates()
      pygame.draw.line(self.screen, BLACK, i.coordinates_start, i.coordinates_end, 3)
    return
  
#   def _get_data_section_elements(self, filename):
#     file = open(filename, "r")
#     # we read in a json object and decode it as Section
#     content = file.read()
#     section = Section.json_decode(content)
#     
#     element_text = section.get_section_display_stripped()
#     
#     return element_text
#   
#   # we need this because pygames font can't handle newlines
#   def _display_data_section_elements(self, filename, x, y):
#     element_text = self._get_data_section_elements(filename)
#     messages = element_text.split()
#     # loop so that all lines are displayed correclty
#     for i in messages:
#       label = self.font.render(i, 1, BLACK)
#       chart.screen.blit(label, (x, y))
#       y = y + self.font_size
      
  def print(self):
    print("from file ", self.source_file)
    
    print("users")
    for i in self.column_users:
      print(i)
    
    print("data column")
    for i in self.column_data:
      print(i)
    
    print("party column")
    for i in self.column_parties:
      print(i)
    
    print("all edges")
    for i in self.edges:
      print(i.to_string())
  

if __name__ == '__main__':
  
  chart = Chart("Response_Data/list_of_responses.txt")
  chart.init()
  chart.print()
  
  # Loop until the user clicks the close button.
  done = False

  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()

  # -------- Main Program Loop -----------
  while not done:
    #--- Main event loop
    for event in pygame.event.get(): # User did something
      if event.type == pygame.QUIT: # If user clicked close
        done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here
  
    # --- Drawing code should go here
  
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    chart.screen.fill(WHITE)
    
    chart.draw_nodes()
    chart.draw_edges()
    
    # pygame.draw.line(chart.screen, BLACK, (55,70), (55,95), 5)

    # pygame.draw.rect(chart.screen, RED, [55, 50, 20, 25])
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    