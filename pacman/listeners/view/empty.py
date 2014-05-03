class EmptyViewListener:
  def on_draw(self, event):
    (x, y, view) = event
    screen = view.screen
    emptyImage = view.emptyImage

    emptyRect = emptyImage.get_rect().move((x*view.WIDTH, y*view.HEIGHT))
    screen.blit(emptyImage, emptyRect)