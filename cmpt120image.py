# Create some helper functions to wrap the
# Pygame image functions

import pygame
import numpy

def getImage(filename):
  """
  Input: filename - string containing image filename to open
  Returns: 2d array of RGB values
  """
  image = pygame.image.load(filename)
  return pygame.surfarray.array3d(image).tolist()

def saveImage(pixels, filename):
  """
  Input:  pixels - 2d array of RGB values
          filename - string containing filename to save image
  Output: Saves a file containing pixels
  """
  nparray = numpy.asarray(pixels)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, colours) = nparray.shape
  surf = pygame.display.set_mode((width, height))
  pygame.surfarray.blit_array(surf, nparray)
  pygame.image.save(surf, filename)

def showImage(pixels, title):
    """
    Input:  pixels - 2d array of RGB values
            title - title of the window
    Output: show the image in a window
    """
    nparray = numpy.asarray(pixels)
    surf = pygame.surfarray.make_surface(nparray)
    (width, height, colours) = nparray.shape
    pygame.display.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode((width, height))
    screen.fill((225, 225, 225))
    screen.blit(surf, (0, 0))
    pygame.display.update()

def createBlackImage(width, height):
    """
    Input:  width - width of the filled image in pixels
            height - height of the filled image in pixels
    Output: 2d array of RGB values all set to zero
    """
    return numpy.zeros((width, height, 3)).tolist()