import pygame;

class Sprite:
  FRAME_SPEED = 0.4
  def __init__(self, name, startX, startY, width, height, spriteImage, maxFrames):
    self.name = name
    self.startX = startX
    self.startY = startY
    self.width = width
    self.height = height
    self.spriteImage = spriteImage
    self.maxFrames = maxFrames
    self.frames = self.get_frames()

  def get_image(self, x, y):
    image = pygame.Surface([self.width, self.height]).convert_alpha()
    image.blit(self.spriteImage, (0, 0), (x, y, self.width, self.height))
    image.set_colorkey((0, 0, 0))
    return image

  def get_frame(self, frame):
    return self.frames[frame]

  def get_frames(self):
    frames = []
    i = 0

    while i < 6:
      frames.append(self.get_image(self.startX + (i*self.width), self.startY))
      i += 1
    return frames

  def next_frame(self, animal):
    animal.frame += self.FRAME_SPEED
    if (animal.frame > len(self.frames)-1):
      animal.frame = 0

    return self.get_frame(int(animal.frame))