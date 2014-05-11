import pygame;
import numpy

class Sprite:
  FRAME_SPEED = 0.4
  def __init__(self, name, startX, startY, width, height, spriteImage, maxFrames, grayscale = False):
    self.name = name
    self.startX = startX
    self.startY = startY
    self.width = width
    self.height = height
    self.spriteImage = spriteImage
    self.maxFrames = maxFrames
    self.grayscale = grayscale
    self.frames = self.get_frames()

  def get_image(self, x, y):
    image = pygame.Surface([self.width, self.height]).convert_alpha()
    image.blit(self.spriteImage, (0, 0), (x, y, self.width, self.height))
    image.set_colorkey((0, 0, 0))
    return image

  def make_grayscale(self, image):
    arr = pygame.surfarray.array3d(image)
    avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
    arr = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
    return pygame.surfarray.make_surface(arr)

  def get_frame(self, frame):
    return self.frames[frame]

  def get_frames(self):
    frames = []
    i = 0

    while i < 6:
      image = self.get_image(self.startX + (i*self.width), self.startY)
      if self.grayscale:
        image = self.make_grayscale(image)
      frames.append(image)
      i += 1
    return frames

  def next_frame(self, animal):
    animal.frame += self.FRAME_SPEED
    if (animal.frame > len(self.frames)-1):
      animal.frame = 0

    return self.get_frame(int(animal.frame))