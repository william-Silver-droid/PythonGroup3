import pygame
import random
import numpy as np
import time
import csv
import utils
class Utils():
  def run():
    np.multiply(1, 1)
    pygame.init()
    screen = pygame.display.set_mode(size=(600, 600))
    pygame.display.set_caption('Text in Pygame')
    
    # Set up the font
    font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the size
    
    # Create a text surface
    text = font.render('Hello, Pygame!', True, (255, 255, 255))  # text, antialiasing, color
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Clear the screen
        screen.fill((0, 0, 0))
    
        # Blit the text surface onto the screen
        screen.blit(text, (100, 100))
    
        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()
    def split_multi_word_items(lst):
      new_lst = []
      for item in lst:
          if ' ' in item:
              new_lst.extend(item.split())
          else:
              new_lst.append(item)
      return new_lst
      
    def load_words():
      terms = []
      
    
      for i in range(5):
        terms = split_multi_word_items(terms)
    
    
      # Path to the output CSV file
      csv_file_path = 'words.csv'
    
      # Write the data to the CSV file
      with open(csv_file_path, mode='w', newline='') as csvfile:
          csvwriter = csv.writer(csvfile)
          csvwriter.writerow(['Term'])
          csvwriter.writerows([[term] for term in terms])
    
      print(f"Data written to {csv_file_path}")
    