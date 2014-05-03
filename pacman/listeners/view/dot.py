class DotViewListener:
  def on_draw(self, event):
    (x, y, view) = event
    screen = view.screen
    dotImage = view.dotImage

    dotRect = dotImage.get_rect().move((x*view.WIDTH, y*view.HEIGHT))
    screen.blit(dotImage, dotRect)