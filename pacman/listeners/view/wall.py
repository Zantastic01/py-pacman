class WallViewListener:
  def on_draw(self, event):
    (x, y, view) = event
    screen = view.screen
    wallImage = view.wallImage

    wallRect = wallImage.get_rect().move((x*view.WIDTH, y*view.HEIGHT))
    screen.blit(wallImage, wallRect)