'''
Created on Jan 20, 2017

@author: Lili
'''

from src.Section_Collector import Section_Collector

import pygame
pygame.init()

class Questionnaire(object):
    
  # create questionnaire with sections from section list
  def __init__(self, filename):
    self.sections_for_collection = []
    # read in section names to be constructed
    with open(filename, 'r') as f:
      content = f.readlines()
    # create an array of section collector objects
    for i in range(0, len(content)):
      file_path = "Questionnaire_Data/section_" + content[i].strip() + ".txt"
      collector = Section_Collector(file_path)
      self.sections_for_collection.append(collector)
      
  def start_questionnaire(self):
    for i in self.sections_for_collection:
      i.ask_section()
      i.store_responses("graphics/Response_Data")
      
  def _button_press(self):
    return
      
  
if __name__ == '__main__':
  #q = Questionnaire("Questionnaire_Data/list_of_sections.txt")
  #q.start_questionnaire()
  
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
      elif event.type == pygame.MOUSEBUTTONDOWN:
        print("down")
      elif event.type == pygame.MOUSEBUTTONUP:
        print("up")

    # --- Game logic should go here
  
    # --- Drawing code should go here
  
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    